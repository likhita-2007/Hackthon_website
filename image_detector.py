
import streamlit as st
import google.generativeai as genai
from PIL import Image
from gtts import gTTS  # New Import
import os

# 1. Setup
def image_detector_ui():
    genai.configure(api_key="AIzaSyBiZ0gu9QS4efECmnC8zBOrbSaOCIYfbXk")
    model = genai.GenerativeModel('models/gemini-2.5-flash')

# 2. Frontend
    st.title("AI Image Detector")

    st.info(" Upload any image of a person, document, or object to check if it's AI-generated.")


    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
    
        if st.button("Analyze Image"):
            with st.spinner("Analyzing and preparing audio..."):
                try:
                # 3. AI Analysis Logic
                    prompt = """
                    You are a friendly AI detective. 
                    1. Look at the image. 
                    2. Tell me if it looks like AI-generated (Yes/No). 
                    3. Explain why in simple, friendly, non-technical language.
                    4. Keep it short.

                    """
                    response = model.generate_content([prompt, image])
                    result_text = response.text
                
                # 4. Show the text
                    st.subheader("Analysis Result:")
                    st.write(result_text)
                                # 5. Voice Logic (The Add-on)
                    tts = gTTS(text=result_text, lang='en')
                    tts.save("analysis.mp3")
                    st.audio("analysis.mp3", format="audio/mp3")
                
                except Exception as e:
                    st.error(f"Something went wrong: {e}")


           
# 6. Privacy Footer
    st.markdown("---")
    st.caption("🔒 **Privacy Notice:** We do not save your images. Your image is sent to Google's AI for analysis and is deleted immediately.")