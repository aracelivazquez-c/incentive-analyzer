import streamlit as st
import pandas as pd
import openai
import os

# -------------------------
# CONFIGURACIÓN OPENAI API
# -------------------------
openai.api_key = os.getenv("OPENAI_API_KEY")  # Obtener la API Key desde las variables de entorno

# -------------------------
# TÍTULO Y DESCRIPCIÓN
# -------------------------
st.title("📊 Incentive Analyzer AI")
st.write("""
Carga tus datos mensuales de transacciones y esquema de bonos, y deja que la IA analice tendencias, sugiera mejoras y te alerte sobre posibles problemas.
""")

# -------------------------
# INPUTS DEL USUARIO
# -------------------------
# 1. Subir archivo CSV
uploaded_file = st.file_uploader("Carga tu archivo de transacciones (CSV)", type=['csv'])

# 2. Texto libre: descripción del esquema de bonos
bono_text = st.text_area("Describe aquí el sistema de bonos y objetivos clave de este mes", height=200)

# 3. Opcional: Métricas clave
metrics = st.text_input("¿Cuáles son las métricas clave a mejorar este mes? (separadas por comas)")

# -------------------------
# PROCESAMIENTO DE DATOS
# -------------------------
if uploaded_file and bono_text:
    df = pd.read_csv(uploaded_file)
    st.subheader("Vista previa de datos")
    st.dataframe(df.head())

    # Procesamiento básico
    st.write("Resumen estadístico rápido:")
    st.write(df.describe())

    # -------------------------
    # ENVÍO A OPENAI (LLM)
    # -------------------------
    st.subheader("🔎 Análisis Inteligente")

    # Preparar prompt
    prompt = f"""
Actúa como un analista de incentivos. Aquí está el esquema de bonos:

{bono_text}

Estas son las métricas clave que la organización busca mejorar:
{metrics}

Aquí están los datos de transacciones del mes (columnas: {', '.join(df.columns)}):
{df.head(20).to_csv(index=False)} 

Por favor:
1. Detecta tendencias importantes (positivas o negativas).
2. Señala cualquier patrón preocupante.
3. Sugiere ajustes al sistema de bonos para mejorar las métricas clave.
4. Lanza cualquier advertencia si es necesario.
"""

    with st.spinner("Analizando con IA..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        analysis = response['choices'][0]['message']['content']
        st.success("¡Análisis completado!")
        st.markdown(analysis)

    # -------------------------
    # DESCARGAR REPORTE (Opcional)
    # -------------------------
    st.download_button("Descargar reporte", analysis, file_name="incentive_report.txt")

else:
    st.info("Carga tus datos y descripción para comenzar.")
