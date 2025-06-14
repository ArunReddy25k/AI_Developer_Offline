import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="AI Dev Agent (Offline)", layout="wide")

st.title("🧠 AI Developer Agent (Ollama Powered)")
st.markdown("Ask me to write code, debug programs, or solve DSA problems in any programming language!")

# Check Ollama connection
def check_ollama_connection():
    try:
        response = requests.get("http://localhost:11434")
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

# Check button
if st.button("🧪 Check Ollama Connection"):
    if check_ollama_connection():
        st.success("✅ Ollama is running and connected!")
    else:
        st.error("❌ Could not connect to Ollama. Please make sure you have run:\n\n`ollama run llama3` in another terminal.")

# Prompt box
prompt = st.text_area("📝 What do you want help with?", height=200)

# Submit button
if st.button("🚀 Submit Prompt"):
    if not check_ollama_connection():
        st.error("❌ Ollama is not connected. Please run: `ollama run llama3` in another terminal.")
    elif not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": "llama3",
                        "prompt": prompt,
                        "stream": False
                    }
                )
                result = response.json()
                st.success("✅ Response:")
                st.code(result.get("response", "No response received."), language="python")
            except Exception as e:
                st.error(f"❌ Failed to communicate with LLM: {e}")
