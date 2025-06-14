import streamlit as st
import platform
from openai import OpenAI

# Optional voice output (only runs locally)
def speak_text(text):
    if platform.system() != "Linux":  # Avoid running on Streamlit Cloud
        try:
            import pyttsx3
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print("Voice error (optional):", e)
    else:
        print("🔇 Voice not supported in cloud.")

# Streamlit UI
st.set_page_config(page_title="AI Dev Agent", layout="wide")
st.title("🧠 AI Developer Agent + DSA Solver")

st.markdown("Ask me to write code, debug programs, or solve DSA problems in any programming language!")

api_key = st.text_input("🔑 Enter your OpenAI API Key", type="password")

if not api_key:
    st.warning("Please enter your OpenAI API key to use this agent.")
    st.stop()

prompt = st.text_area("📝 What do you want help with?", height=200)

if st.button("🚀 Submit"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Thinking..."):
            try:
                client = OpenAI(api_key=api_key)

                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )

                answer = response.choices[0].message.content
                st.success("✅ Response:")
                st.code(answer, language='python')

                speak_text(answer)  # Optional voice output

            except Exception as e:
                st.error(f"❌ Error: {e}")
