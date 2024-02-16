import json
from mmf.mmf.models.mmbt import MMBT
model = MMBT.from_pretrained("mmbt.hateful_memes.images")

# Detect whether the meme is hatefuo or not
def hateful_memes_detection(url, txt, threshold = 0.9):
    try:
        output = model.classify(url, txt)
        hateful = True if output["label"] == 1 else False
        if(hateful == True and output['confidence'] > threshold):
            return "Hateful"
    except:
        return txt
    return txt

if __name__ == "__main__":
    root = "../MemeCraft/"
    cot = "COT"
    # For Climate Action
    # focus_dic = {"Supporter": ["Causes", "Consequences", "Solutions"], "Denier": ["Evidence of Absence", "Benefits"]}
    # For Gender Equality
    focus_dic = {"Supporter": ["Causes", "Consequences", "Solutions"], "Denier": ["Evidence of Absence", "Rationale"]}
    for supporter in ["Supporter", "Denier"]:  # "Supporter"
        for context in focus_dic[supporter]:
            for model_name in ["LLaMA", "ChatGPT", "LLaVA"]:
                if(model_name == "LLaVA"):
                    cot = "Non-COT"
                else:
                    cot = "COT"
                print("Current is " + model_name + " " + context)
                image_text_path = root + "meme_image_dataset/gender_inequality_memes/imgflip_"+ model_name +"/gender_inequality_" + supporter + "_" + context + "_"  + cot + "_caption.json"
                image_url_path = root + "meme_image_dataset/imgflip_image_name_url_backup.json"
                with open(image_text_path, "r") as f:
                    data = json.load(f)
                with open(image_url_path, "r") as f:
                    url_data = json.load(f)
                for img in data:
                    url = url_data[img][0]
                    txt = data[img][0]
                    if(txt != "Error" and txt != "Hateful"):
                        raw_txt = txt
                        txt = hateful_memes_detection(url, txt)
                        data[img][0] = txt
                        if(txt == "Hateful"):
                            print("Hateful")
                            print(img)
                            print(raw_txt)
                            with open(image_text_path, "w") as f:
                                json.dump(data,f)

