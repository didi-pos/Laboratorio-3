import streamlit as st
import requests
from gtts import gTTS
import os

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
            {"role": "system", "content": 'Eres Nikola Tesla con una actitud bastante inteligente y clara con lo que explica.'},
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

# --- Streamlit UI ---
st.title("💬 Chatbot de DeepSeek - Nikola Tesla")
st.write("Haz una pregunta sobre sistemas digitales y escucha la respuesta.")

# Guardar historial de conversación
if "historial" not in st.session_state:
    st.session_state.historial = []

# Entrada del usuario
entrada = st.text_input("Escribe tu pregunta:")

if st.button("Enviar") and entrada:
    respuesta = enviar_mensaje(entrada)
    st.session_state.historial.append(("Tú", entrada))
    st.session_state.historial.append(("Chatbot", respuesta))

    # Generar voz de la respuesta
    audio_file = generar_audio(respuesta)
    st.audio(audio_file, format="audio/mp3")

# Mostrar historial
for rol, texto in st.session_state.historial:
    if rol == "Tú":
        st.markdown(f"**{rol}:** {texto}")
    else:
        st.markdown(f"**🤖 {rol}:** {texto}")
