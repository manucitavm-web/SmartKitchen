import streamlit as st
            "Agregar pasta",
            "Cocinar durante 10 minutos",
            "Servir"
        ]
    },
    "arroz": {
        "ingredients": ["Arroz", "Agua", "Sal"],
        "steps": [
            "Agregar agua",
            "Agregar arroz",
            "Cocinar 20 minutos"
        ]
    }
}

if recipe.lower() in recipes:
    data = recipes[recipe.lower()]

    st.success(f"Receta encontrada: {recipe}")

    st.subheader("Ingredientes")
    for ingredient in data["ingredients"]:
        st.write(f"✅ {ingredient}")

    st.subheader("Pasos")
    for i, step in enumerate(data["steps"]):
        st.write(f"{i+1}. {step}")

    if st.button("▶️ Iniciar modo cocina"):
        st.info("Modo cocina activado")

        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.02)
            progress.progress(i + 1)

        st.success("Receta completada")

else:
    st.warning("Busca una receta como: pasta o arroz")

st.divider()

st.subheader("🎙️ Simulación de comandos de voz")

voice_command = st.selectbox(
    "Selecciona un comando",
    [
        "Siguiente paso",
        "Repetir receta",
        "Activar temporizador",
        "Finalizar receta"
    ]
)

if st.button("Ejecutar comando"):
    st.success(f"Comando ejecutado: {voice_command}")
