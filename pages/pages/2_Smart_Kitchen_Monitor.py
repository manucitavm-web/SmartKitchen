import streamlit as st
import random
import time

st.title("🔥 Smart Kitchen Monitor")

st.subheader("Estado de sensores")

temperature = random.randint(25, 100)

st.metric("Temperatura actual", f"{temperature} °C")

if temperature > 70:
    st.error("⚠️ Temperatura muy alta")
    st.audio("https://www.soundjay.com/buttons/beep-01a.mp3")
else:
    st.success("✅ Temperatura estable")

st.divider()

st.subheader("Estado de dispositivos")

led_status = st.toggle("Estufa inteligente")

if led_status:
    st.success("🔥 Estufa ENCENDIDA")
else:
    st.info("⭕ Estufa APAGADA")

fan_status = st.toggle("Extractor de humo")

if fan_status:
    st.success("💨 Extractor ACTIVADO")

st.divider()

st.subheader("Temporizador")

minutes = st.slider("Selecciona minutos", 1, 60, 5)

if st.button("Iniciar temporizador"):

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.03)
        progress.progress(i + 1)

    st.success("⏰ Tiempo finalizado")
