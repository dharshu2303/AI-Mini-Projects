import google.generativeai as genai 
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-2.5-flash")
st.title("Blog Generator")
prompt=st.text_input("Enter your Blog Topic here..")
res="you are a blog generator, write a blog on user asked content with sub topics and in story related way, " \
"make it more engaging and interesting to read"
if st.button("Submit"):
    response=model.generate_content([res,prompt])
    st.write(response.text)         