import streamlit as st
import google.generativeai as genai

# Page Title
st.title("YouTube AI वीडियो स्टूडियो")

# API Key handling
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # Aapki list mein uplabdh model: gemini-2.0-flash
    model = genai.GenerativeModel('gemini-2.0-flash')
except Exception as e:
    st.error(f"Configuration Error: {e}")
    st.stop()

# Input
topic = st.text_input("वीडियो का टॉपिक लिखें:")

if st.button("स्क्रिप्ट जनरेट करें"):
    if not topic:
        st.warning("कृपया टॉपिक लिखें!")
    else:
        try:
            with st.spinner('स्क्रिप्ट लिख रहा हूँ...'):
                response = model.generate_content(f"YouTube के लिए {topic} पर एक बेहतरीन स्क्रिप्ट लिखें")
                st.markdown(response.text)
        except Exception as e:
            st.error(f"एरर आ गया: {e}")
            
