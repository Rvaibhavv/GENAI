from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os 
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



model =genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)

    return response.text

st.set_page_config(page_title="Q&A demo")
st.header("gemini llm application")
input =st.text_input("input: ",key='input')
submit =st.button("ask the question")

if submit:
    respone = get_gemini_response(input)
    st.subheader("the response is")
    st.write(respone)