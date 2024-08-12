import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

url = "https://api-b2b.backenster.com/b1/api/v3/translate"
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": API_KEY
}

st.title("Basic Translation App")

text_input = st.text_area("Enter text to translate:")

# Define language options with user-friendly names
language_options = {
    "English (US)": "en_US",
    "English (Great Britain)": "en_GB",
    "Myanmar (Burmese)": "my_MM",
    "Russian": "ru_RU",
    "Hindi": "hi_IN",
    "Bengali": "bn_BD",
    "Japanese": "ja_JP",
    "Korean": "ko_KR",
    "Thai": "th_TH",
    "Chinese (Simplified)": "zh-Hans_CN",  # Corrected code
    "French": "fr_FR",
    "Spanish": "es_ES",
    "German": "de_DE",
    "Portuguese (Brazil)": "pt_BR",
    "Portuguese": "pt_PT",
    "Arabic": "ar_SA",
   # Add more languages here as needed
}

# Create selectboxes with user-friendly names
source_language = st.selectbox("Select source language:", list(language_options.keys()))
target_language = st.selectbox("Select target language:", list(language_options.keys()))

if st.button("Translate"):
    if text_input:
        # Get language codes from selected options
        source_code = language_options[source_language]
        target_code = language_options[target_language]

        payload = {
            "platform": "api",
            "data": text_input,
            "from": source_code,
            "to": target_code,
            "enableTransliteration": True
        }
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            try:
                translation = response.json()["result"]
                st.success("Translation:")
                st.write(translation)

                # Add copy button
                st.code(translation)
                if st.button("Copy Translation"):
                    st.query_params(translation=translation)
            except KeyError:
                st.error("Error: Unexpected API response format. Please check the API documentation.")
                print(response.json())
        else:
            st.error(f"Error translating text. Status code: {response.status_code}")
            print(response.text)
    else:
        st.warning("Please enter text to translate.")

# Check for copied translation in query parameters
if "translation" in st.query_params:
    copied_translation = st.query_params["translation"][0]
    st.success("Translation copied to clipboard!")
    st.write(copied_translation)
