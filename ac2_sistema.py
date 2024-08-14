import speech_recognition as sr
import streamlit as st

st.title("fale...")

recognizer = Sr.Microphone()
mic = sr.Microphone()

with mic as source:
    audio = recognizer.listen(source)
text = recognizer.recognize_google(audio, language="pt-BR")
st.write("você disse:" + text)
