
import streamlit as st
from PIL import Image
import pytesseract
import pandas as pd
import io
import re

st.title("📄 Extrator de Dados de PNG")

uploaded_files = st.file_uploader("Envie as imagens .png", type="png", accept_multiple_files=True)

dados_extraidos = []

if uploaded_files:
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)

        # Extração de texto com Tesseract
        texto = pytesseract.image_to_string(image, lang='por')

        # Inicializa os campos
        no_servico = re.search(r"No\.?Serviço[:\s]*([0-9]+)", texto)
        km_final = re.search(r"KM Final[:\s]*([0-9\.,]+)", texto)
        total_devido = re.search(r"Total/Devido R\$[:\s]*([0-9\.,]+)", texto)

        dados_extraidos.append({
            "Arquivo": uploaded_file.name,
            "No. Serviço": no_servico.group(1) if no_servico else "",
            "KM Final": km_final.group(1) if km_final else "",
            "Total/Devido R$": total_devido.group(1) if total_devido else "",
        })

    df = pd.DataFrame(dados_extraidos)
    st.dataframe(df)

    # Gerar Excel para download
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Serviços')

    st.download_button(
        label="📥 Baixar Excel",
        data=output.getvalue(),
        file_name="servicos_mprj.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
