import streamlit as st
from transformers import pipeline
import re
from gtts import gTTS
import io

def apply_clean_style():
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF !important; background-image: none !important; }
        
        [data-testid="stTextArea"] textarea {
            background-color: #F0F2F6 !important; 
            /* CHANGE: Font color to Dark Grey */
            color: #333333 !important;
            border-radius: 10px !important;
            border: 1px solid #E2E8F0 !important;
        }

        /* CHANGE: Specifically target the 'Paste message here...' placeholder color */
        [data-testid="stTextArea"] textarea::placeholder {
            color: #555555 !important;
            opacity: 1;
        }

        .stButton>button {
            background-color: #F0F2F6 !important;
            color: #000000 !important;
            font-weight: 600 !important;
        }
        [data-testid="stNotificationContent"], .stAlert p { color: #000000 !important; }
        </style>
    """, unsafe_allow_html=True)

@st.cache_resource
def load_ai():
    return pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-sms-spam-detection")

def message_detector_ui():
    apply_clean_style()
    st.markdown("<h2 style='color: #2D3748;'>🔍 AI Message Detector</h2>", unsafe_allow_html=True)
    
    user_input = st.text_area("input", placeholder="Paste message here...", label_visibility="collapsed", height=150)
    
    if st.button("Scan Content"):
        if user_input.strip():
            classifier = load_ai()
            res = classifier(user_input)[0]
            is_scam = res['label'] == 'LABEL_1' or "http" in user_input.lower()
            
            verdict = "Verdict: High Risk. Potential Scam detected." if is_scam else "Verdict: Safe. No immediate risk."
            if is_scam: st.error(verdict)
            else: st.success(verdict)
            
            tts = gTTS(text=verdict, lang='en')
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            st.audio(audio_fp, format='audio/mp3')