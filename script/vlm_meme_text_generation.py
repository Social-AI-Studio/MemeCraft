
import argparse
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
import os
from llava.conversation import conv_templates, SeparatorStyle
from llava.utils import disable_torch_init
from transformers import CLIPVisionModel, CLIPImageProcessor, StoppingCriteria
from llava.model import *
from llava.model.utils import KeywordsStoppingCriteria
import json
from PIL import Image
from prompt_demo import  generation_question
import os
import requests
from PIL import Image
from io import BytesIO
import re

def prompt_generation(supporter, context, demo_number=4):
    demo = ""
    generation_question_demo = generation_question.replace("<Stance2>", supporter.replace("Supporter", "support").replace("Denier", "deny")).replace("<Context>", context)
    demo += generation_question_demo \
                + 'Output: "'
    return demo 

def calculate_median(lst):
    sorted_lst = sorted(lst, reverse=True)
    n = len(sorted_lst)
    
    middle = n // 2
    median = sorted_lst[middle]
    
    return median

def output_retrieve(text):
    if('"' in text):
        pattern = r'"(.*?)"'
        results = re.findall(pattern, text)
        results = [s for s in results if len(s.split()) < 30 and len(s.split()) > 3 ]
        if(results):
            selected_string = calculate_median(results)
            return selected_string
        else:
            return "Error"
    return "Error"


DEFAULT_IMAGE_TOKEN = "<image>"
DEFAULT_IMAGE_PATCH_TOKEN = "<im_patch>"
DEFAULT_IM_START_TOKEN = "<im_start>"
DEFAULT_IM_END_TOKEN = "<im_end>"


def load_image(image_file):
    if image_file.startswith('http') or image_file.startswith('https'):
        response = requests.get(image_file)
        image = Image.open(BytesIO(response.content)).convert('RGB')
    else:
        image = Image.open(image_file).convert('RGB')
    return image

def generate_caption(input_ids, temperature , image_tensor, stopping_criteria, stop_str):
        with torch.inference_mode():
            output_ids = model.generate(
                input_ids,
                images=image_tensor.unsqueeze(0).half().cuda(),
                do_sample=True,
                temperature=1,
                max_new_tokens=200,
                stopping_criteria=[stopping_criteria])

        input_token_len = input_ids.shape[1]
        n_diff_input_output = (input_ids != output_ids[:, :input_token_len]).sum().item()
        if n_diff_input_output > 0:
            print(f'[Warning] {n_diff_input_output} output_ids are not the same as the input_ids')
        outputs = tokenizer.batch_decode(output_ids[:, input_token_len:], skip_special_tokens=True)[0]
        outputs = outputs.strip()
        if outputs.endswith(stop_str):
            outputs = outputs[:-len(stop_str)]
        outputs = outputs.strip()
        return output_retrieve(outputs), outputs

def eval_model(model_name, data, supporter, context, output_path = "", conv_mode = None):
    mm_use_im_start_end = getattr(model.config, "mm_use_im_start_end", False)
    tokenizer.add_tokens([DEFAULT_IMAGE_PATCH_TOKEN], special_tokens=True)
    if mm_use_im_start_end:
        tokenizer.add_tokens([DEFAULT_IM_START_TOKEN, DEFAULT_IM_END_TOKEN], special_tokens=True)

    vision_tower = model.get_model().vision_tower[0]
    if vision_tower.device.type == 'meta':
        vision_tower = CLIPVisionModel.from_pretrained(vision_tower.config._name_or_path, torch_dtype=torch.float16, low_cpu_mem_usage=True).cuda()
        model.get_model().vision_tower[0] = vision_tower
    else:
        vision_tower.to(device='cuda', dtype=torch.float16)
    vision_config = vision_tower.config
    vision_config.im_patch_token = tokenizer.convert_tokens_to_ids([DEFAULT_IMAGE_PATCH_TOKEN])[0]
    vision_config.use_im_start_end = mm_use_im_start_end
    if mm_use_im_start_end:
        vision_config.im_start_token, vision_config.im_end_token = tokenizer.convert_tokens_to_ids([DEFAULT_IM_START_TOKEN, DEFAULT_IM_END_TOKEN])
    image_token_len = (vision_config.image_size // vision_config.patch_size) ** 2

    if os.path.exists(output_path):
        with open(output_path, "r") as f:
            results = json.load(f)
    else:   
        results ={}
    for name in data:
        if(name in results):
            outputs = results[name][0]
            if(outputs != "Error"):
                continue
        else:
            outputs = "Error"
        
        query = prompt_generation(supporter, context)
        qs = query
        try:
            image = load_image(data[name][0].replace("////", "//"))
        except:
            print("Error")
            continue
        if mm_use_im_start_end:
            qs = qs + '\n' + DEFAULT_IM_START_TOKEN + DEFAULT_IMAGE_PATCH_TOKEN * image_token_len + DEFAULT_IM_END_TOKEN
        else:
            qs = qs + '\n' + DEFAULT_IMAGE_PATCH_TOKEN * image_token_len

        if "v1" in model_name.lower():
            conv_mode = "llava_v1"
        elif "mpt" in model_name.lower():
            conv_mode = "mpt_multimodal"
        else:
            conv_mode = "multimodal"
        conv = conv_templates[conv_mode].copy()
        conv.append_message(conv.roles[0], qs)
        conv.append_message(conv.roles[1], None)
        prompt = conv.get_prompt()
        inputs = tokenizer([prompt])

        image_tensor = image_processor.preprocess(image, return_tensors='pt')['pixel_values'][0]

        input_ids = torch.as_tensor(inputs.input_ids).cuda()

        stop_str = conv.sep if conv.sep_style != SeparatorStyle.TWO else conv.sep2
        keywords = [stop_str]
        stopping_criteria = KeywordsStoppingCriteria(keywords, tokenizer, input_ids)

        i = 0
        while(outputs == "Error" and i <= 3):
            i+=1
            outputs, unfiltered_outputs = generate_caption(input_ids,i , image_tensor, stopping_criteria, stop_str)
        print("Final caption is " + outputs)
        results[name]= [outputs, unfiltered_outputs]
        with open(output_path, "w") as f:
            json.dump(results, f)
        

if __name__ == "__main__":
    root = "../MemeCraft/"
    input_path = root + "dataset/meme_template_sorted.json"
    with open(input_path, "r") as f:
        data = json.load(f)

    # For Climate Action
    # focus_dic = {"Supporter": ["Causes", "Consequences", "Solutions"], "Denier": ["Evidence of Absence", "Benefits"]}
    # For Gender Equality
    focus_dic = {"Supporter": ["Causes", "Consequences", "Solutions"], "Denier": ["Evidence of Absence", "Rationale"]}

    model_name = "liuhaotian/LLaVA-Lightning-MPT-7B-preview"
    # Load model directly
    disable_torch_init()
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    if "mpt" in model_name.lower():
        model = LlavaMPTForCausalLM.from_pretrained(model_name, low_cpu_mem_usage=True, torch_dtype=torch.float16, use_cache=True).cuda()
    else:
        model = LlavaLlamaForCausalLM.from_pretrained(model_name, low_cpu_mem_usage=True, torch_dtype=torch.float16, use_cache=True).cuda()
    image_processor = CLIPImageProcessor.from_pretrained(model.config.mm_vision_tower, torch_dtype=torch.float16)

    for cot in ["Non-COT"]:
        for supporter in ["Supporter", "Denier"]: 
            for context in focus_dic[supporter]:
                for model_name in ["LLaVA"]:
                        # For Climate Action
                        # image_text_path =  root + "dataset/climate_action_memes/imgflip_"+ model_name +"/climate_change_" + supporter + "_" + context + "_"  + cot + "_caption.json"
                        # For Gender Equality
                        image_text_path =  root + "dataset/gender_inequality_memes/imgflip_"+ model_name +"/gender_inequality_" + supporter + "_" + context + "_"  + cot + "_caption.json"
                        if(context == "Rationale"):
                            eval_model(model_name, data["Benefits"], supporter, context, image_text_path)
                        else:
                            eval_model(model_name, data[context], supporter, context, image_text_path)

