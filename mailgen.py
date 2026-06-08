import google.generativeai as genai 
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model=genai.GenerativeModel("gemini-2.5-flash")
st.title("Mail Generator")
sender = st.text_input("From:")
recipient = st.text_input("To:")
subject = st.text_input("Subject:")

res = "Draft a highly professional email based on these details and if the  subject is for the friendly email then make it more casual and engaging. " \
      "Make sure to include a proper greeting and closing, and keep the tone appropriate for the context of the email."

if st.button("Generate"):
    prompt = f"From: {sender}\nTo: {recipient}\nSubject: {subject}"
    response = model.generate_content([res, prompt])
    st.write(response.text)