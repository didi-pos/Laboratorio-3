import streamlit as st
import requests
from gtts import gTTS
import os
from streamlit_mic_recorder import speech_to_text

API_KEY = os.getenv("DEEPSEEK_API_KEY")
API_URL = "https://api.deepseek.com/v1/chat/completions"

def enviar_mensaje(mensaje, modelo="deepseek-chat"):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": modelo,
        "messages": [
            {"role": "system", "content": "Eres Nikola Tesla con una actitud bastante inteligente y clara con lo que explica."},
            {"role": "user", "content": mensaje},
        ],
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.text}"

def generar_audio(texto, filename="respuesta.mp3"):
    tts = gTTS(text=texto, lang="es")
    tts.save(filename)
    return filename

st.title("💬 Chatbot de Voz de DeepSeek - Nikola Tesla")
st.write("Haz una pregunta sobre sistemas digitales y escucha la respuesta.")

if "historial" not in st.session_state:
    st.session_state.historial = []

entrada_texto = st.text_input("Escribe tu pregunta:")
st.write("O usa tu voz:")
entrada_voz = speech_to_text(language="es", just_once=True, use_container_width=True, key="voz")

entrada = entrada_texto if entrada_texto else entrada_voz

if st.button("Enviar") and entrada:
    respuesta = enviar_mensaje(entrada)
    st.session_state.historial.append(("Tú", entrada))
    st.session_state.historial.append(("Chatbot", respuesta))
    audio_file = generar_audio(respuesta)
    st.audio(audio_file, format="audio/mp3")

for rol, texto in st.session_state.historial:
    if rol == "Tú":
        st.markdown(f"**{rol}:** {texto}")
    else:
        st.markdown(f"**🤖 {rol}:** {texto}")
