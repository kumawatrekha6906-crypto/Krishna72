import streamlit as st
import google.generativeai as genai

# Page Title
st.title("YouTube AI वीडियो स्टूडियो")

# API Key handling
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # Using the stable model name
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    st.error(f"API Key या कॉन्फ़िगरेशन में एरर: {e}")
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
            
