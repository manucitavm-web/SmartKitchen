import streamlit as st

st.set_page_config(
    page_title="SmartKitchen",
    page_icon="🍳",
    layout="wide"
)

st.title("🍳 SmartKitchen Home Assistant")

st.markdown("""
## Bienvenido a SmartKitchen

Una cocina inteligente multimodal que permite:
- interacción por voz
- monitoreo de sensores
- temporizadores
- automatización
- alertas inteligentes
""")

st.image("assets/kitchen.jpeg")

st.info("Usa el menú lateral para navegar entre páginas.")
