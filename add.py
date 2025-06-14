import streamlit as st
import subprocess
import requests
import platform

# Optional: voice (only on local machine)
def speak_text(text):
    if platform.system() != "Linux":  # skip voice in cloud
        try:
            import pyttsx3
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print("Voice error (optional):", e)

# Setup Streamlit UI
st.set_page_config(page_title="Offline AI Developer", layout="wide")
st.title("💻 AI Developer Agent (No OpenAI)")

st.markdown("Write code, debug, and solve DSA using a local LLM (via Ollama).")

prompt = st.text_area("🧠 Ask anything:", height=200)

if st.button("🚀 Run"):
    if prompt.strip() == "":
        st.warning("Enter a prompt first.")
    else:
        with st.spinner("Thinking with local LLM..."):
            try:
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": "llama3",  # or any model available in Ollama
                        "prompt": prompt,
                        "stream": False
                    }
                )

                result = response.json()["response"]
                st.success("✅ Response:")
                st.code(result, language="python")
                speak_text(result)

            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.info("Is Ollama running? Start it with a model like `ollama run llama3`.")

