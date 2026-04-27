import streamlit as st
import google.generativeai as genai

st.title("YouTube AI वीडियो स्टूडियो")

# Secrets से Key लें
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # 1.5-flash के लिए लेटेस्ट लाइब्रेरी का इस्तेमाल
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Secrets सेटिंग्स में API Key चेक करें!")
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
