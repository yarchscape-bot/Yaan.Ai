import streamlit as st
from google import genai
from google.genai import types

# Page Config (Luxury Studio Standard)
st.set_page_config(page_title="YAAN.AI // Spatial Generative Canvas", layout="wide", initial_sidebar_state="collapsed")

# Core Responsive Master Stylesheet
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap');

/* Base Styles */
.stApp { background-color: #000000 !important; color: #d1cbc4 !important; font-family: 'Plus Jakarta Sans', sans-serif; }
div[data-testid="stDecoration"] { display: none; }
textarea { background-color: #08080c !important; color: #ffffff !important; border: 1px solid rgba(209, 203, 196, 0.09) !important; border-radius: 6px; padding: 10px; }
div[data-testid="stForm"] { border: none !important; padding: 0 !important; }

/* Desktop Master Layout rules */
.gendo-studio-header { display: flex; justify-content: space-between; align-items: center; padding: 24px 48px; border-bottom: 1px solid rgba(209, 203, 196, 0.08); background-color: #000000; margin-bottom: 40px; gap: 20px; }
.gendo-brand-main { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 2.2rem; font-weight: 700; letter-spacing: 1px; color: #ffffff; line-height: 1.1; }
.gendo-brand-tagline { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 0.85rem; font-weight: 400; color: #888888; margin-top: 6px; letter-spacing: 0.5px; }
.gendo-brand-founder { font-family: 'Space Grotesk', sans-serif; font-size: 0.75rem; font-weight: 400; color: #555555; margin-top: 4px; letter-spacing: 1px; }
.gendo-brand-founder a { color: #888888; text-decoration: none; border-bottom: 1px dashed rgba(136,136,136,0.3); }
.gendo-brand-founder a:hover { color: #ffffff; }
.gendo-status-node { font-family: 'Space Grotesk', sans-serif; font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase; color: #888888; border: 1px solid rgba(209, 203, 196, 0.15); padding: 6px 16px; background: rgba(255, 255, 255, 0.02); white-space: nowrap; }
.gendo-hero-title { font-family: 'Space Grotesk', sans-serif; font-size: 4.8rem; font-weight: 400; letter-spacing: -3px; text-align: center; color: #ffffff; margin-top: 20px; }
.gendo-hero-sub { font-size: 1.15rem; color: #7a7a7a; text-align: center; margin-bottom: 60px; font-weight: 300; padding: 0 20px; }
.gendo-studio-panel { background: rgba(3, 3, 5, 0.9); border: 1px solid rgba(209, 203, 196, 0.07); border-radius: 8px; padding: 35px; margin-bottom: 30px; }
.gendo-executive-footer { width: 100%; text-align: center; padding: 50px 0; margin-top: 100px; border-top: 1px solid rgba(209, 203, 196, 0.07); font-family: 'Space Grotesk', sans-serif; font-size: 0.9rem; letter-spacing: 4px; color: #666666; text-transform: uppercase; }
.gendo-executive-badge { color: #ffffff; font-weight: 700; letter-spacing: 5px; margin-left: 8px; }

@media screen and (max-width: 768px) {
    .gendo-studio-header { flex-direction: column; align-items: flex-start; padding: 20px; margin-bottom: 25px; gap: 15px; }
    .gendo-status-node { align-self: flex-start; width: auto; font-size: 0.65rem; padding: 4px 10px; white-space: normal; }
    .gendo-hero-title { font-size: 2.4rem; }
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
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
st.markdown("<h1 class='gendo-hero-title'>Spatial Generative Studio</h1>", unsafe_allow_html=True)
st.markdown("<p class='gendo-hero-sub'>Autonomous blueprint diagnostic engine and academic tracking matrices</p>", unsafe_allow_html=True)

# --- WORKSPACE ---
col_left, col_right = st.columns(2, gap="large")

with col_left:
    st.markdown("<div class='gendo-studio-panel'>", unsafe_allow_html=True)
    with st.form(key="ai_form", clear_on_submit=False):
        user_prompt = st.text_area("Ask YAAN.AI (English/Hindi/Gujarati)...", height=150)
        trigger_execution = st.form_submit_button("EXECUTE COMPUTATION FLOW")
    st.markdown("</div>", unsafe_allow_html=True)

with col_right:
    st.markdown("<div class='gendo-studio-panel'>", unsafe_allow_html=True)
    if trigger_execution and user_prompt:
        API_KEY = "AIzaSyCelu_k9VJDAwMvK4XhmgHtiAXH7YCBotQ"
        
        # GUJARATI LANGUAGE ADDED HERE
        system_instruction = """
        You are YAAN.AI, a premium spatial engineering and architectural AI specialist. 
        Language Rules: 
        1. Always respond in the SAME language the user asks (English, Hindi, or Gujarati).
        2. If the user asks in Gujarati, you MUST reply in Gujarati.
        3. Keep answers professional, accurate, and helpful for Gujarat academic/real estate contexts. No emojis.
        """
        
        with st.spinner("Processing architectural data layers..."):
            try:
                client = genai.Client(api_key=API_KEY)
                # Stable Model Used
                response = client.models.generate_content(
                    model='gemini-1.5-flash',
                    contents=user_prompt,
                    config=types.GenerateContentConfig(system_instruction=system_instruction)
                )
                st.write(response.text)
            except Exception as e:
                st.error(f"System Operational Exception: {str(e)}")
    else:
        st.info("System Idle. Enter your query on the left.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.write("---")
st.markdown(f'<div class="gendo-executive-footer">SYSTEM CONTROL CORE OPERATED BY CHIEF EXECUTIVE FOUNDER: <span class="gendo-executive-badge">MR KEVIL SOLANKI</span></div>', unsafe_allow_html=True)
