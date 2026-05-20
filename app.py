import streamlit as st
from google import genai
from google.genai import types

# Page Config
st.set_page_config(page_title="YAAN.AI", layout="wide")

# UI Logic
col_left, col_right = st.columns(2, gap="large")

with col_left:
    with st.form(key="ai_form"):
        user_prompt = st.text_area("Ask YAAN.AI (English/Hindi/Gujarati)...", height=150)
        # Button trigger
        submitted = st.form_submit_button("EXECUTE COMPUTATION FLOW")

with col_right:
    # Logic tabhi chalega jab button click hoga
    if submitted and user_prompt:
        try:
            # Secrets se key secure tarike se uthana
            client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
            
            # Instruction
            system_instruction = "You are YAAN.AI, a specialist. Respond in the language asked (English, Hindi, or Gujarati). No emojis."
            
            with st.spinner("Processing..."):
                response = client.models.generate_content(
                    model='gemini-1.5-flash',
                    contents=user_prompt,
                    config=types.GenerateContentConfig(system_instruction=system_instruction)
                )
                st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.info("System Idle. Enter your query.")
