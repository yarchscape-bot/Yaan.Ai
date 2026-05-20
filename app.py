import streamlit as st
from google import genai
from google.genai import types

# Page Config (Luxury Studio Standard)
st.set_page_config(page_title="YAAN.AI // Spatial Generative Canvas", layout="wide", initial_sidebar_state="collapsed")

# Core Responsive Master Stylesheet
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght=300;400;500;600;700&family=Plus+Jakarta+Sans:wght=300;400;500;600&display=swap');

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

/* 📱 Fluid Mobile Responsiveness Framework */
@media screen and (max-width: 768px) {
    .gendo-studio-header { flex-direction: column; align-items: flex-start; padding: 20px; margin-bottom: 25px; gap: 15px; }
    .gendo-status-node { align-self: flex-start; width: auto; font-size: 0.65rem; padding: 4px 10px; white-space: normal; }
    .gendo-brand-main { font-size: 1.8rem; }
    .gendo-brand-tagline { font-size: 0.75rem; }
    .gendo-brand-founder { font-size: 0.7rem; }
    .gendo-hero-title { font-size: 2.4rem; letter-spacing: -1px; margin-top: 10px; line-height: 1.2; }
    .gendo-hero-sub { font-size: 0.95rem; margin-bottom: 35px; }
    .gendo-studio-panel { padding: 20px; margin-bottom: 20px; }
    .gendo-executive-footer { font-size: 0.7rem; letter-spacing: 2px; padding: 30px 10px; }
    .gendo-executive-badge { letter-spacing: 2px; display: block; margin-top: 5px; }
    div[data-testid="column"] { width: 100% !important; flex: 1 1 100% !important; }
    .stTable { display: block; overflow-x: auto; }
}
</style>
""", unsafe_allow_html=True)

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

st.markdown("<h1 class='gendo-hero-title'>Spatial Generative Studio</h1>", unsafe_allow_html=True)
st.markdown("<p class='gendo-hero-sub'>Autonomous blueprint diagnostic engine and academic tracking matrices</p>", unsafe_allow_html=True)

# --- SIDE-BY-SIDE PLATFORM WORKSPACE ---
col_left, col_right = st.columns(2, gap="large")

with col_left:
    st.markdown("<div class='gendo-studio-panel'>", unsafe_allow_html=True)
    st.markdown('<h3 style="color:#fff; font-family:\'Space Grotesk\'; margin-top:0; font-size:1.4rem;">AI Terminal Core</h3>', unsafe_allow_html=True)
    with st.form(key="ai_form", clear_on_submit=False):
        user_prompt = st.text_area("Ask YAAN.AI (e.g., Explain CEPT portfolio submission guidelines or Adani Realty infrastructure layouts)...", height=150)
        trigger_execution = st.form_submit_button("EXECUTE COMPUTATION FLOW")
    st.markdown("</div>", unsafe_allow_html=True)

with col_right:
    st.markdown("<div class='gendo-studio-panel'>", unsafe_allow_html=True)
    st.markdown('<h3 style="color:#fff; font-family:\'Space Grotesk\'; margin-top:0; font-size:1.4rem;">AI Engine Stream Output</h3>', unsafe_allow_html=True)
    if trigger_execution and user_prompt:
        API_KEY = "AIzaSyBFr1Yv3vyASdom-MdrhPUhwTuBlPDlPvs"
        
        system_instruction = "You are YAAN.AI, a premium spatial engineering and architectural AI specialist built by Executive Chief Founder Mr Kevil Solanki. Keep your answers ultra-professional, mathematically accurate, and specifically helpful for Gujarat academic universities (CEPT, Nirma, MSU, SCET, etc.) and real estate corporates (Adani, Shivalik, Avadh). Do not use emojis."
        
        with st.spinner("Processing architectural data layers..."):
            try:
                # Initializing Official Google GenAI Native Client
                client = genai.Client(api_key=API_KEY)
                
                response = client.models.generate_content(
                    model='gemini-1.5-flash',
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction
                    )
                )
                
                if response.text:
                    st.write(response.text)
                else:
                    st.warning("Engine computed an empty response structure.")
            except Exception as e:
                st.error(f"System Operational Exception: {str(e)}")
    else:
        st.info("System Idle. Enter your query on the left and execute the engine flow.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- DIRECTORIES DATA MATRIX ---
st.write("---")
st.markdown('<h2 style="text-align:center; font-family:\'Space Grotesk\'; font-weight:300; color:#ffffff; margin-bottom:20px;">Institutional & Corporate Environments</h2>', unsafe_allow_html=True)

tab_academics, tab_corporates = st.tabs(["Gujarat Academic Repository Matrix", "Real Estate Enterprise Directories"])

with tab_academics:
    st.markdown("<br>", unsafe_allow_html=True)
    ac_data = [
        {"University Node": "CEPT University, Ahmedabad", "Core Studio Focus": "Advanced Urbanism, Transit Hub Design", "Jury Defense Parameter": "High focus on volumetric density and circulation math"},
        {"University Node": "Nirma University", "Core Studio Focus": "High-Rise Structures, Lateral Load Integrity", "Jury Defense Parameter": "Demands rigid structural stability calculations"},
        {"University Node": "MSU Baroda", "Core Studio Focus": "Heritage Conservation & Vernacular Forms", "Jury Defense Parameter": "Requires clean measured drawings and history logs"},
        {"University Node": "SCET, Surat", "Core Studio Focus": "Coastal Urban Habitats, Flood Resilience", "Jury Defense Parameter": "Contextual planning adaptations for tidal baselines"}
    ]
    st.table(ac_data)

with tab_corporates:
    st.markdown("<br>", unsafe_allow_html=True)
    corp_data = [
        {"Enterprise Node": "Adani Realty", "Chief Executive / Founder": "Mr. Gautam Adani", "Portfolio Domain Focus": "Mega-scale industrial townships & high-volume smart cities"},
        {"Enterprise Node": "Shivalik Group", "Chief Executive / Founder": "Mr. Chitrak Shah", "Portfolio Domain Focus": "Iconic high-rise downtown commercial properties & zero-column facades"},
        {"Enterprise Node": "Avadh Group", "Chief Executive / Founder": "Mr. Lavjibhai Daliya (Badshah)", "Portfolio Domain Focus": "Premium luxury lifestyle schemes & macro Vastu layout systems"},
        {"Enterprise Node": "Bakeri Group", "Chief Executive / Founder": "Mr. Anil Bakeri", "Portfolio Domain Focus": "Pioneering horizontal housing townships & passive micro-grids"}
    ]
    st.table(corp_data)

# --- SIGNATURE FOOTER ---
st.markdown(f'<div class="gendo-executive-footer">SYSTEM CONTROL CORE OPERATED BY CHIEF EXECUTIVE FOUNDER: <span class="gendo-executive-badge">MR KEVIL SOLANKI</span></div>', unsafe_allow_html=True)
