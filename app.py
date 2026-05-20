import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="YAAN.AI", layout="wide")

# CSS (Keep your existing styles here...)

# --- LAYOUT ---
st.markdown("<h1 class='gendo-hero-title'>YAAN.AI</h1>", unsafe_allow_html=True)

col_left, col_right = st.columns(2)

with col_left:
    with st.form(key="ai_form"):
        user_prompt = st.text_area("Ask YAAN.AI...")
        trigger_execution = st.form_submit_button("EXECUTE")

with col_right:
    if trigger_execution: # Ab yeh scope ke andar hai
        if not user_prompt:
            st.warning("Please enter a prompt.")
        else:
            try:
                # Secret se secure fetch
                api_key = st.secrets.get("GEMINI_API_KEY")
                if not api_key:
                    st.error("API Key not found in secrets!")
                else:
                    client = genai.Client(api_key=api_key)
                    
                    # Model name correct karke 'gemini-1.5-flash' use kiya hai
                    response = client.models.generate_content(
                        model='gemini-1.5-flash',
                        contents=user_prompt,
                        config=types.GenerateContentConfig(
                            system_instruction="You are YAAN.AI. Reply in English, Hindi, or Gujarati based on user input. Maintain professional architectural tone."
                        )
                    )
                    st.write(response.text)
            except Exception as e:
                st.error(f"System Error: {str(e)}")
