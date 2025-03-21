# Incentive Analyzer AI

Esta es una aplicación de Streamlit que utiliza la API de OpenAI para analizar incentivos y tendencias dentro de los pagos de transacciones y sistemas de bonos. Puedes cargar los datos de transacciones de tu empresa y obtener recomendaciones automáticas sobre cómo mejorar el esquema de incentivos.

## Instrucciones

1. **Sube tu archivo CSV** con las transacciones y pagos de los agentes.
2. **Describe el sistema de bonos** que estás utilizando y las métricas clave que deseas mejorar.
3. La app enviará los datos a la API de OpenAI para un análisis profundo.
4. Obtendrás un reporte con sugerencias y alertas, ¡listo para mejorar tu sistema de incentivos!

## Requisitos

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/incentive-analyzer-ai.git
    ```
2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3. Asegúrate de tener configurada tu clave de API de OpenAI en el archivo `.streamlit/secrets.toml`.

4. Para correr la aplicación localmente:
    ```bash
    streamlit run app.py
    ```

## Despliegue en Streamlit Cloud

1. Crea una cuenta en [Streamlit Cloud](https://streamlit.io/cloud).
2. Conecta tu repositorio de GitHub o GitLab.
3. Agrega tu **API Key de OpenAI** en **Streamlit Cloud** a través de la sección **Secrets**.
4. Haz clic en "Deploy" y tu aplicación estará lista.

## Licencia

MIT License. Consulta el archivo LICENSE para más detalles.
