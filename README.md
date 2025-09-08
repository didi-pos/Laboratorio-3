<h1 align="center">Laboratorio-3: Chatbot y Despliegue</h1>

<p align="center">
  Proyecto de Ingeniería Electrónica - Universidad Santo Tomás<br>
  Bogotá, Colombia
</p>

<h2>Resumen</h2>
<p>
Este laboratorio tiene como objetivo implementar un <strong>chatbot interactivo</strong> utilizando la API de 
<a href="https://api.deepseek.com" target="_blank">DeepSeek</a>. 
Se desarrollaron dos versiones principales:
</p>

<ul>
  <li><strong>Chatbot en consola:</strong> responde directamente mediante texto en la terminal.</li>
  <li><strong>Chatbot en Streamlit con audio:</strong> permite interacción visual y genera respuestas habladas usando la librería <code>gTTS</code>.</li>
</ul>

<h2>Proceso de despliegue</h2>
<p>
El despliegue del chatbot se realizó paso a paso:
</p>
<ol>
  <li>Preparación del código en <strong>Visual Studio Code</strong>, configurando la API Key en el archivo Python.</li>
  <li>Instalación de librerías necesarias con <code>pip install requests streamlit gtts</code>.</li>
  <li>Creación de un repositorio en <strong>GitHub</strong> para alojar el proyecto (<code>Laboratorio-3</code>).</li>
  <li>Vinculación del repositorio con <strong>Streamlit Cloud</strong> y despliegue de la aplicación.</li>
  <li>Edición y actualización del chatbot directamente desde la nube, con posibilidad de ejecución tanto en consola como en entorno gráfico.</li>
</ol>

<h2>Conclusión</h2>
<p>
Al finalizar, se obtuvo un chatbot funcional capaz de responder de manera clara y sencilla sobre temas de sistemas digitales. 
Además, la versión en audio mejora la accesibilidad y la interacción del usuario.
</p>

<section style="font-family: system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; max-width:900px; margin:24px auto;">
  <h2 style="text-align:center; color:#0f1720;">Aplicaciones desplegadas</h2>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:18px; margin-top:16px;">
    <article style="background:#0b1220; border-radius:12px; padding:18px; color:#f1f5f9; box-shadow:0 6px 18px rgba(2,6,23,0.6);">
      <h3 style="margin:0 0 8px 0; font-size:20px;">Chatbot en Streamlit.app</h3>
      <p style="margin:0 0 12px 0; color:#cbd5e1; line-height:1.4;">
        Interfaz web de preguntas y respuestas sobre sistemas digitales. Incluye historial y salida de audio.
      </p>
      <a href="https://laboratorio-3-igbcgsjcpkcjgbmzt6dznb.streamlit.app/" target="_blank" rel="noopener" style="display:inline-block; padding:8px 12px; border-radius:8px; background:linear-gradient(90deg,#2DB1C4,#0242A3); color:white; text-decoration:none; font-weight:600;">Abrir app →</a>
    </article>
    <article style="background:#0b1220; border-radius:12px; padding:18px; color:#f1f5f9; box-shadow:0 6px 18px rgba(2,6,23,0.6);">
      <h3 style="margin:0 0 8px 0; font-size:20px;">Chatbot de voz en Streamlit.app</h3>
      <p style="margin:0 0 12px 0; color:#cbd5e1; line-height:1.4;">
        Versión con entrada por micrófono y conversión a texto para interactuar por voz con el chatbot.
      </p>
      <a href="https://laboratorio-3-jmhy2puho7dfqkvvrwkyhm.streamlit.app/" target="_blank" rel="noopener" style="display:inline-block; padding:8px 12px; border-radius:8px; background:linear-gradient(90deg,#8B5CF6,#06B6D4); color:white; text-decoration:none; font-weight:600;">Abrir app →</a>
    </article>
  </div
  <p style="text-align:center; color:#94a3b8; margin-top:14px; font-size:13px;">
    Abre en una nueva pestaña. Requiere micrófono para la versión de voz.
  </p>
</section>
