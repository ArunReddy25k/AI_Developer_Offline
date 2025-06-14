import streamlit as st
import requests

st.set_page_config(page_title="Free AI Dev Agent", layout="wide")
st.title("💻 AI Dev Agent — Powered by Ollama (No OpenAI Required)")

st.markdown("Write code, debug, and solve DSA problems with a local LLM.")

prompt = st.text_area("🧠 Ask your AI Agent something:", height=200)

if st.button("🚀 Submit"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Thinking using Ollama..."):
            try:
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": "llama3",     # Or another model like "mistral" or "codellama"
                        "prompt": prompt,
                        "stream": False
                    }
                )
                result = response.json().get("response", "")
                st.success("✅ Response:")
                st.code(result, language="python")
            except Exception as e:
                st.error(f"❌ Could not connect to Ollama.\n\nError: {e}")
                st.info("Make sure you ran: `ollama run llama3` in your terminal.")
