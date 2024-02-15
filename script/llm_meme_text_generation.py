# !pip install git+https://github.com/huggingface/transformers
# !pip install ipywidgets
# !pip install openai

import openai
import json
import time
from PIL import Image, ImageDraw, ImageFont
import random
import pandas as pd
import re
import os
import nltk
from nltk.stem import PorterStemmer
from google_images_search import GoogleImagesSearch
import html
import urllib.request
import io
import textwrap
import csv
import transformers
import torch
import shutil
from langdetect import detect
from prompt_demo import image_selection_pools, context_string, generation_question
from PIL import Image
import requests
from transformers import Blip2Processor
from transformers import Blip2ForConditionalGeneration
from io import BytesIO


# tokenizer = transformers.LlamaTokenizer.from_pretrained("meta-llama/Llama-2-13b-hf", use_auth_token = "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")
# model = transformers.LlamaForCausalLM.from_pretrained("meta-llama/Llama-2-13b-hf", use_auth_token = "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", device_map="auto", torch_dtype=torch.float16)

def prompt_generation_llama(name, caption, supporter, context, demo_number):

    demo = context_string[supporter][context]
    generation_question_demo = generation_question.replace("<Stance>", supporter).replace("<Context>", context)
    i = 0
    for image in image_selection_pools[supporter][context]:
        i += 1
        if(i > demo_number):
            break
        Name = image["Name"]
        Caption = image["Caption"]
        Text = image["Text"]
    
        demo += generation_question_demo  \
                +  'Input: Image "'+ Name+'" describing "' + Caption + '" \n' \
                + 'Output: Caption: "' + Text + '" \n'
    demo += generation_question_demo  \
                +  'Input: Image "'+ name+'" describing "' + caption + '" \n' \
                + 'Output: Caption: "' 
    return demo 


def prompt_generation_cot_llama(name, caption, supporter, context, demo_number):
    demo= ""
    generation_question_demo = generation_question.replace("<Stance>", supporter).replace("<Stance2>", supporter.replace("Supporter", "support").replace("Denier", "deny")).replace("<Context>", context)
    i = 0
    for image in image_selection_pools[supporter][context]:
        i += 1
        if(i > demo_number):
            break
        Name = image["Name"]
        Caption = image["Caption"]
        COT = image["COT"]
        Text = image["Text"]
    
        demo += generation_question_demo  \
                +  'Input: Image "'+ Name+'" describing "' + Caption + '" \n' \
                + 'Output: Let\'s think step by step. ' + COT + ' Caption: "' + Text + '" \n'
    demo += generation_question_demo  \
                +  'Input: Image "'+ name+'" describing "' + caption + '" \n' \
                + 'Output: Let\'s think step by step. '
    return demo 


def prompt_generation_gpt(name, caption, supporter, context, demo_number):

    demo = context_string[supporter][context]
    generation_question_demo = generation_question.replace("<Stance>", supporter).replace("<Context>", context)
    i = 0
    for image in image_selection_pools[supporter][context]:
        i += 1
        if(i > demo_number):
            break
        Name = image["Name"]
        Caption = image["Caption"]
        Text = image["Text"]

        demo += generation_question_demo  \
                    +  'Input: Image "'+ Name+'" describing "' + Caption + '" \n' 

        if(" - " in Text):
            caption_top = Text.split(" - ")[0]
            caption_bottom = Text.split(" - ")[1]
            demo += 'Output: Caption at top: "' + caption_top + '" and Caption at bottom: "' + caption_bottom + '" \n'
        else:
            demo += 'Output: Caption at top: "' + Text + '" \n'
    demo += generation_question_demo  \
                +  'Input: Image "'+ name+'" describing "' + caption + '" \n' \
                + 'Output: Caption at top: "' 
    return demo 


def prompt_generation_cot_gpt(name, caption, supporter, context, demo_number):
    demo= ""
    generation_question_demo = generation_question.replace("<Stance>", supporter).replace("<Stance2>", supporter.replace("Supporter", "support").replace("Denier", "deny")).replace("<Context>", context)
    i = 0
    for image in image_selection_pools[supporter][context]:
        i += 1
        if(i > demo_number):
            break
        Name = image["Name"]
        Caption = image["Caption"]
        COT = image["COT"]
        Text = image["Text"]
        demo += generation_question_demo  \
                +  'Input: Image "'+ Name+'" describing "' + Caption + '" \n' 

        if(" - " in Text):
            caption_top = Text.split(" - ")[0]
            caption_bottom = Text.split(" - ")[1]
            demo += 'Output: Let\'s think step by step. ' + COT + ' Caption at top: "' + caption_top + '" and Caption at bottom: "' + caption_bottom + '" \n'
        else:
            demo += 'Output: Let\'s think step by step. ' + COT + ' Caption at top: "' + Text + '" \n'
        
            
    demo += generation_question_demo  \
                +  'Input: Image "'+ name+'" describing "' + caption + '" \n' \
                + 'Output: Let\'s think step by step. '
    return demo 

def gpt_output_retrieve(text, demo_number):
    pattern = r"{0}(.*?){1}".format('Caption at top: "', '"')
    match = re.search(pattern, text, re.DOTALL)

    processed_caption = ""
    if match:
        caption_top = match.group(1).strip()
    else:
        return "Error"
    processed_caption += caption_top
    if("Caption at bottom: \"" in text):
        pattern = r"{0}(.*?){1}".format('Caption at bottom: "', '"')
        match = re.search(pattern, text, re.DOTALL)
        if match:
            caption_bottom = match.group(1).strip()
        else:
            caption_bottom = text.split('Caption at bottom: "')[-1]
        processed_caption += " <-> " +  caption_bottom

    return processed_caption

def llama_output_retrieve(text, demo_number):
    if("\nOutput:" in text):
        text = text.split("\nOutput:")[demo_number + 1]
    pattern = r"{0}(.*?){1}".format('Caption: "', '" \n')
    match = re.search(pattern, text, re.DOTALL)

    processed_caption = ""
    if match:
        caption_top = match.group(1).strip()
    else:
        return "Error"
    processed_caption += caption_top
    return processed_caption


openai.api_key ="API-KEY"
def callChatAPI(content, temperature=1,msgs=None):
    
    retry=0
    response=None
    while retry<3:
        try:
            if msgs is None:    
                msgs=[            
                {
                    "role": "user", "content":content          
                }
                ]
            response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=temperature,    
            messages=msgs
            )
            break
        except:
            retry+=1
            time.sleep(3)
    return response["choices"][0]["message"]["content"]

def call_llama(prompt, temperature=1, max_token=100, device = "cuda:0"):
    # Tokenize the prompt
    batch = tokenizer(
        prompt,
        return_tensors="pt",
        add_special_tokens=False
    )
    # Move the batch to the first GPU
    batch = {k: v.to(device) for k, v in batch.items()}
    generated = model.generate(batch["input_ids"], temperature=temperature, max_new_tokens=max_token)
    # Decode the generated output
    decoded_output = tokenizer.decode(generated[0])
    return decoded_output


root = "../MemeCraft"
image_caption_path =  root + "dataset/meme_text_description.json"
image_url_path = root + "dataset/meme_template_sorted.json"
def run_caption_generation(path, output_path, model_name, supporter, context, cot, demo_number):
    with open(path, "r") as f:
        data = json.load(f)

    with open(image_url_path, "r") as f:
        if(context == "Rationale"):
            img_url = json.load(f)["Benefits"]
        else:
            img_url = json.load(f)[context]
    sampled_image_list = list(img_url.keys())

    if os.path.exists(output_path):
        with open(output_path, "r") as f:
            output = json.load(f)
    else:   
        output ={}

    for img_name in sampled_image_list:
        if(img_name in output):
            cleaned_text = output[img_name][0]
            if(cleaned_text != "Error" and cleaned_text != "Hateful" ):
                continue
        else:
            cleaned_text = "Error"
        img_caption = data[img_name][0]
        if("." not in img_caption):
            img_caption =img_caption.split(".")[0]

        if(cot == "COT"):
            if(model_name == "ChatGPT"):
                prompt = prompt_generation_cot_gpt(img_name, img_caption , supporter, context, demo_number)
            else:
                prompt = prompt_generation_cot_llama(img_name, img_caption , supporter, context, demo_number)
        else:
            if(model_name == "ChatGPT"):
                prompt = prompt_generation_gpt(img_name, img_caption , supporter, context, demo_number)
            else:
                prompt = prompt_generation_llama(img_name, img_caption , supporter, context, demo_number)
        i = 0 
        while((cleaned_text == "Error" or cleaned_text == "Hateful")and i <= 3):
            i += 1
            if(model_name == "ChatGPT"):
                text = callChatAPI(prompt)
                cleaned_text = gpt_output_retrieve(text, demo_number)
            else:
                text = call_llama(prompt, 1, 200)
                cleaned_text = llama_output_retrieve(text, demo_number)
            print(text)
            print(cleaned_text)
        output[img_name] = [cleaned_text, text]
        with open(output_path, "w") as f:
            json.dump(output, f)



# For Climate Action
# focus_dic = {"Supporter": ["Causes", "Consequences", "Solutions"], "Denier": ["Evidence of Absence", "Benefits"]}
# For Gender Equality
focus_dic = {"Supporter": ["Causes", "Consequences", "Solutions"], "Denier": ["Evidence of Absence", "Rationale"]}

if __name__ == "__main__":
    for cot in ["COT"]:
        for supporter in ["Supporter", "Denier"]:
            for context in focus_dic[supporter]:
                for model_name in ["ChatGPT", "LLaMA"]:
                    for demo_number in range(4, 5, 2):
                        print("demo number is " + str(demo_number))
                        # For Climate Action
                        # image_text_path =  root + "dataset/climate_action_memes/imgflip_"+ model_name +"/climate_change_" + supporter + "_" + context + "_"  + cot + "_caption.json"
                        # For Gender Equality
                        image_text_path =  root + "dataset/gender_inequality_memes/imgflip_"+ model_name +"/gender_inequality_" + supporter + "_" + context + "_"  + cot + "_caption.json"
                        run_caption_generation(image_caption_path, image_text_path, model_name, supporter, context, cot, demo_number)


