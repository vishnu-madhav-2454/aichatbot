import os
import json
import google.generativeai as genai



working_directory= os.path.dirname(os.path.abspath(__file__))
config_json_path = f'{working_directory}/config.json'
config_data= json.load(open(config_json_path))
GOOGLE_API_KEY= config_data['GOOGLE_API_KEY']

genai.configure(api_key = GOOGLE_API_KEY)


def load_model():
    gemini_pro_model = genai.GenerativeModel('gemini-1.0-pro')
    return gemini_pro_model

def load_model_1(prompt,image):
    gemini_pro_model_vision = genai.GenerativeModel('gemini-pro-vision')
    response = gemini_pro_model_vision.generate_content([prompt,image])
    return response.text
