import streamlit as st
import subprocess
import pyttsx3
import speech_recognition as sr
import os

st.set_page_config(page_title="💡 Offline AI Dev Agent", layout="wide")
st.title("🧠 Offline AI Developer Agent (LLaMA/Mistral)")
st.markdown("Write code, debug, or solve DSA problems – totally offline!")

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Voice input
use_voice = st.checkbox("🎙️ Use voice input")

prompt = ""
if use_voice:
    st.info("Click the button and speak your prompt.")
    if st.button("🎤 Record"):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            prompt = r.recognize_google(audio)
            st.success(f"You said: {prompt}")
        except:
            st.error("Sorry, could not recognize your voice.")
else:
    prompt = st.text_area("📝 What do you want help with?", height=200)

# Run local LLM
if st.button("🚀 Run with Local AI"):
    if not prompt.strip():
        st.warning("Please enter something.")
    else:
        with st.spinner("Thinking (local model)..."):
            try:
                result = subprocess.run(
                    ["ollama", "run", "llama3", prompt],
                    capture_output=True, text=True, timeout=120
                )
                response = result.stdout.strip()
                st.success("✅ Response:")
                st.code(response, language="python")

                # Add to chat history
                st.session_state.history.append({"user": prompt, "ai": response})

                # Speak out loud
                tts = pyttsx3.init()
                tts.say(response)
                tts.runAndWait()
            except Exception as e:
                st.error(f"Error: {e}")

# Display chat history
if st.session_state.history:
    st.markdown("### 💬 Chat History")
    for chat in reversed(st.session_state.history):
        st.markdown(f"**You:** {chat['user']}")
        st.markdown(f"**AI:** {chat['ai']}")
