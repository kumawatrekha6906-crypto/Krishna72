import streamlit as st
import google.generativeai as genai

st.title("YouTube AI वीडियो स्टूडियो")

# Streamlit secrets से API Key लें
api_key = st.secrets["GEMINI_API_KEY"]

topic = st.text_input("वीडियो का टॉपिक लिखें:")

if st.button("स्क्रिप्ट जनरेट करें"):
    if not topic:
        st.warning("कृपया टॉपिक लिखें!")
    else:
        try:
            genai.configure(api_key=api_key)
            
            # यहाँ हमने मॉडल का नाम अपडेट कर दिया है जो काम करेगा
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            response = model.generate_content(f"YouTube के लिए {topic} पर एक बेहतरीन स्क्रिप्ट लिखें")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"कुछ गलत हो गया: {e}")
