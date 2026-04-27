import streamlit as st
import google.generativeai as genai

st.title("YouTube AI वीडियो स्टूडियो")

# API Key यहाँ मांगेंगे
api_key = st.text_input("अपनी Google Gemini API Key डालें:", type="password")
topic = st.text_input("वीडियो का टॉपिक लिखें:")

if st.button("स्क्रिप्ट जनरेट करें"):
    if not api_key:
        st.error("कृपया अपनी API Key डालें!")
    elif not topic:
        st.warning("कृपया टॉपिक लिखें!")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(f"YouTube के लिए {topic} पर एक बेहतरीन स्क्रिप्ट और वीडियो आइडिया लिखो।")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"कुछ गलत हो गया: {e}")
