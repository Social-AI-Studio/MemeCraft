# -*- coding: utf-8 -*-
# # !pip install git+https://github.com/huggingface/transformers
# # !pip install ipywidgets
# # !pip install openai
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
# from google_images_search import GoogleImagesSearch
import html
import urllib.request
import io
import textwrap
import csv
import requests
import torch
from io import BytesIO
import requests
import urllib
import requests
from bs4 import BeautifulSoup

username = 'username'
password = 'password'
userAgent = 'userAgent'

root = "../MemeCraft"
image_url_path =root+ "dataset/meme_template_sorted.json"

def meme_template_retrieveal(image_url_path):
    data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
    images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]

    output = {}
    for img in images:
        output[img['name']] = [img["url"], img['id']]
    with open(image_url_path, "w") as f:
        json.dump(output, f)

def search_meme(img_name_list, output_path, output):
    for img_name in img_name_list:
        URL = 'https://api.imgflip.com/search_memes'
        params = {
            'username':username,
            'password':password,
            'query':img_name,
        }
        response = requests.request('POST',URL,data=params).json()
        if(response["success"] == True and len(response['data']['memes']) >= 1):
            meme_id = response['data']['memes'][0]['id']
            meme_url = response['data']['memes'][0]['url']
            output[img_name] = [meme_url, meme_id]
            print(response)
            print(len(output))
            # with open(output_path, "w") as f:
            #     json.dump(output, f)
            if(len(output) == 1500):
                break
        
def get_online_memes(data): 
    for context in data:
        for image in data[context]:
            meme_id = data[context][image][1]
            url = "https://imgflip.com/meme/" + meme_id

            response = requests.get(url)
            if response.status_code == 200:
                # Parse the HTML content of the page using BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find the image tag with the meme image
                img_tag = soup.find('img', {'class': 'base-img'})
                
                if img_tag:
                    # Get the image URL from the 'src' attribute of the image tag
                    image_url = img_tag['src']
                    text = img_tag['alt'].split(" | ")[1].replace("; ", " - ")
                    # Print the image URL
                    print("Meme Image URL:", image_url)
                    print("Meme Image Caption:", text)
                    data[context][image].append({"example_url": image_url, "example_caption": text})
                else:
                    print("Image not found on the page.")
            else:
                print("Failed to fetch the web page. Status code:", response.status_code)
    with open(image_url_path, "w") as f:
        json.dump(data, f)

# get_online_memes(output)

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
    start_time = time.time()
    root = "../MemeCraft"
    
    # For Climate Action
    # focus_dic = {"Supporter": ["Causes", "Consequences", "Solutions"], "Denier": ["Evidence of Absence", "Benefits"]}
    # For Gender Equality
    focus_dic = {"Supporter": ["Causes", "Consequences", "Solutions"], "Denier": ["Evidence of Absence", "Rationale"]}
    
    for cot in [ "COT"]: 
        for supporter in ["Denier", "Supporter"]:
            for context in focus_dic[supporter]:
                for model_name in ["LLaVA", "LLaMA","ChatGPT",]: # ,  "LLaMA", "ChatGPT"
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
                        
    end_time = time.time()
    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    print("Elapsed time:", elapsed_time, "seconds")

