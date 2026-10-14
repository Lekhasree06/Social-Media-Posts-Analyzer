
import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


def get_api_key():
    try:
        return st.secrets["GEMINI_API_KEY"]
    except Exception:
        return os.getenv("GEMINI_API_KEY")


def get_gemini_response(prompt: str):
    api_key = get_api_key()

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found. Please set it in Streamlit secrets or environment variable.")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    return response.text
