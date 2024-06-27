from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os 
import google.generativeai as genai
from PIL import Image


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(image,input):

    if input!="":
        response =model.generate_content([image,input])
    else:
        response =model.generate_content(image)
    return response.text


st.header("gemini application")
input = st.text_input("input prompt",key ='input')

upload_file =st.file_uploader("choose an image",type=['jpg',"png"])
image =''
if upload_file is not None:
    image =Image.open(upload_file)
    st.image(image,caption="uplaoded image",use_column_width =True)


submit = st.button("tell me about the image")
if submit:
    response=get_gemini_response(input,image)
    st.subheader("the response is")
    st.write(response)