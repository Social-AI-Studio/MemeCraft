import json
import requests
import requests
import urllib
import requests
import os

username = 'username'
password = 'password'
userAgent = 'userAgent'

# Overlay text to image
def add_caption(id, text0, text1, filename):
    URL = 'https://api.imgflip.com/caption_image'
    params = {
        'username':username,
        'password':password,
        'template_id':id,
        'text0':text0,
        'text1':text1
    }
    try:
        response = requests.request('POST',URL,params=params).json()
        opener = urllib.request.URLopener()
        opener.addheader('User-Agent', userAgent)
    except:
        response = {}
        response["success"] = False
    if(response["success"] == True):
        filename, headers = opener.retrieve(response['data']['url'], filename)


if __name__ == "__main__":
    # Measure the time
    root = "../MemeCraft/"
    image_url_path =root+ "dataset/meme_template_sorted.json"
    
    # For Climate Action
    # focus_dic = {"Supporter": ["Causes", "Consequences", "Solutions"], "Denier": ["Evidence of Absence", "Benefits"]}
    # For Gender Equality
    focus_dic = {"Supporter": ["Causes", "Consequences", "Solutions"], "Denier": ["Evidence of Absence", "Rationale"]}
    
    for cot in [ "COT"]: 
        for supporter in ["Denier", "Supporter"]:
            for context in focus_dic[supporter]:
                for model_name in ["LLaVA", "LLaMA", "ChatGPT",]:
                    if(model_name == "LLaVA"):
                        cot = "Non-COT"
                    else:
                        cot = "COT"
                    image_text_path = root +  "dataset/gender_inequality_memes/imgflip_"+ model_name +"/gender_inequality_" + supporter + "_" + context + "_"  + cot + "_caption.json"
                    
                    with open(image_text_path, "r") as f:
                        data = json.load(f)
                    with open(image_url_path, "r") as f:
                        if(context == "Rationale"):
                            url_data = json.load(f)["Benefits"]
                        else:
                            url_data = json.load(f)[context]
                    
                    for img_name in data:
                        output_filename = root + "meme_image_dataset/gender_inequality_memes/imgflip_" + model_name + "/" +context.replace(" ", "_") + "_" + cot + "/" + img_name.replace("/", "")  + ".jpg"
                        if(img_name not in url_data or data[img_name][0] == "Error" or data[img_name][0] == "Hateful"):
                            if not os.path.exists(output_filename):
                                try:
                                    os.remove(output_filename)
                                except OSError as e:
                                    print(f"Error deleting the file: {e}")
                            print(img_name)
                            print("Invalid caption")
                            continue
                        caption = data[img_name][0]
                        if(" <-> " in caption):
                                text_to_add_top = caption.split(" <-> ")[0]
                                text_to_add_bottom = caption.split(" <-> ")[1]
                        else:
                            if(" - " in caption):
                                text_to_add_top = caption.split(" - ")[0]
                                text_to_add_bottom = caption.split(" - ")[1]
                            else:
                                text_to_add_top = caption
                                text_to_add_bottom = ""
                        id = url_data[img_name][1]
                        print("refresh captions")
                        print(img_name)
                        add_caption(id, text_to_add_top, text_to_add_bottom, output_filename)
                        

