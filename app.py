import streamlit as st
from google import genai
from google.genai import types

# Page Config
st.set_page_config(page_title="YAAN.AI // Spatial Generative Canvas", layout="wide", initial_sidebar_state="collapsed")

# (CSS Wahi purana wala rahega, jo humne pehle set kiya tha)
# ... (Yahan purana CSS copy paste kar dena)

# --- HEADER SECTION ---
header_html = """
<div class="gendo-studio-header">
    <div class="gendo-brand-container">
        <div class="gendo-brand-main">YAAN.AI</div>
        <div class="gendo-brand-tagline">Stories of the [Arts]<br>The Art of Space. The Science of Possibility.&reg;</div>
        <div class="gendo-brand-founder">Meet Kevil : <a href="mailto:kevilhere@gmail.com">kevilhere@gmail.com</a></div>
    </div>
    <div class="gendo-status-node">State-Scale Spatial Intelligence Terminal</div>
</div>
"""
st.markdown(header_html, unsafe_allow_html=True)

# --- AI LOGIC (Update this part) ---
if trigger_execution and user_prompt:
    # Nayi Instruction Matrix
    system_instruction = """
    You are YAAN.AI, a premium spatial engineering and architectural AI specialist built by Executive Chief Founder Mr Kevil Solanki. 
    
    Language Support Protocol: 
    1. Fluently respond in English, Hindi, and Gujarati. 
    2. If a user asks in Gujarati, reply strictly in Gujarati. 
    3. If a user asks in English/Hindi, reply in that language.
    
    Style: Keep answers ultra-professional, mathematically accurate, and specifically helpful for Gujarat academic universities (CEPT, Nirma, MSU, SCET, etc.) and real estate corporates (Adani, Shivalik, Avadh). Do not use emojis.
    """
    
    with st.spinner("Processing architectural data layers..."):
        try:
            # API Key secret se uthana (jaise humne set kiya tha)
            api_key_to_use = st.secrets["GEMINI_API_KEY"]
            client = genai.Client(api_key=api_key_to_use)
            
            # Model name sahi kar diya
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction
                )
            )
            
            if response.text:
                st.write(response.text)
        except Exception as e:
            st.error(f"Error: {str(e)}")
