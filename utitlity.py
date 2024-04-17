import os
import json

import google.generativeai as genai

working_directory = os.path.dirname(os.path.abspath(__file__))

config_path = f"{working_directory}\config.json"
config_data = json.load(open(config_path))

print(config_path,"==>", config_data)

key = config_data["GOOGLE_API_KEY"]

print("Google API key ==>",key)

genai.configure(api_key = key)

def load_model():
    model = genai.GenerativeModel('gemini-pro')
    return model