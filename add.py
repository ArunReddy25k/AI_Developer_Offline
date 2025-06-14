import streamlit as st
import requests

# Streamlit UI setup
st.set_page_config(page_title="🧠 Offline AI Dev Agent", layout="wide")
st.title("🧠 AI Developer Agent (Offline via Ollama)")
st.markdown("Ask me to write code, debug programs, or solve DSA problems in any language!")

# Text input from user
prompt = st.text_area("📝 What do you want help with?", height=200)

# Run when button clicked
if st.button("🚀 Submit"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
        st.stop()

    st.info("🧠 Thinking with llama2:7b...")
    try:
        # Send prompt to Ollama running locally
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "llama2:7b",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )
        data = response.json()
        answer = data["message"]["content"]
        st.success("✅ Response:")
        st.code(answer, language="python")
    except Exception as e:
        st.error(f"❌ Ollama not responding.\n\nError: {e}")
