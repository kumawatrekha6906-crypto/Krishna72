import streamlit as st
import google.generativeai as genai

st.title("YouTube AI चेक टूल")

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("Secrets में GEMINI_API_KEY नहीं मिली!")
else:
    genai.configure(api_key=api_key)
    
    st.write("उपलब्ध मॉडल्स की जांच कर रहा हूँ...")
    try:
        # यहाँ हम देखते हैं कि आपके API Key के लिए कौन से मॉडल्स उपलब्ध हैं
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                st.write(f"- {m.name}")
    except Exception as e:
        st.error(f"API Key काम नहीं कर रही है: {e}")
