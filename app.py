import streamlit as st
import google.generativeai as genai

# Force Update Trigger: 2026-04-28
st.title("YouTube AI वीडियो स्टूडियो")

# Secrets से Key लें
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"API Key एरर: {e}")
    st.stop()

topic = st.text_input("वीडियो का टॉपिक लिखें:")

if st.button("स्क्रिप्ट जनरेट करें"):
    if not topic:
        st.warning("कृपया टॉपिक लिखें!")
    else:
        try:
            response = model.generate_content(f"YouTube के लिए {topic} पर एक बेहतरीन स्क्रिप्ट लिखें")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"एरर आ गया: {e}")
            
