import google.generativeai as genai 
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model=genai.GenerativeModel("gemini-2.5-flash")
st.title("Resume Generator")
edu=st.text_input("Enter your Education details  here..")
exp=st.text_input("Enter your Experience details  here..")
skills=st.text_input("Enter your Skills details  here..")
proj=st.text_input("Enter your Projects details  here..")
res="you are a resume generator, create a professional minimal simple resume based on the provided details within 200 tokens," \
"make sure to include all the relevant information and format it in a clear and organized manner " \
" most importantly ATS Friendly " 
if st.button("Submit"):
    response=model.generate_content([res, edu, exp, skills, proj])
    st.write(response.text)         