import google.generativeai as genai 
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model=genai.GenerativeModel("gemini-2.5-flash")
st.title("AI Code Explainer")
prompt=st.text_input("Enter your code here..")
comm=st.text_input("Enter comments for the code here..")
res="you are an AI code explainer, explain the provided code according to the given comments, " \
"make it easy to understand and follow, explain in a step by step way"
if st.button("Submit"):
    response=model.generate_content([res,prompt,comm])
    st.write(response.text)         