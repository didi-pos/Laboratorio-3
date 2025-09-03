import streamlit as st
import requests
import os

API_KEY = os.getenv("DEEPSEEK_API_KEY")
API_URL = 'https://api.deepseek.com/v1/chat/completions'

def enviar_mensaje(mensaje, modelo='deepseek-chat'):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }

    data = {
        'model': modelo,
        'messages': [
            {'role': 'system', 'content': 'Eres Nikola Tesla con una actitud bastante inteligente y clara con lo que explica.'},
            {'role': 'user', 'content': mensaje}
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as err:
        return f"Error de la API: {err}"
    except Exception as e:
        return f"Error inesperado: {e}"

def main():
    st.title("💬 Chatbot de DeepSeek - Nikola Tesla")
    st.write("Escribe un mensaje y recibe la respuesta del chatbot.")

    if "historial" not in st.session_state:
        st.session_state.historial = []

    mensaje_usuario = st.text_input("Tú:", "")

    if st.button("Enviar") and mensaje_usuario:
        respuesta = enviar_mensaje(mensaje_usuario)
        st.session_state.historial.append(("Tú", mensaje_usuario))
        st.session_state.historial.append(("Chatbot", respuesta))

    for rol, texto in st.session_state.historial:
        st.markdown(f"**{rol}:** {texto}")

if __name__ == "__main__":
    main()

