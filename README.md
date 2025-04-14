
# Extrator de Dados de PNG

Este é um aplicativo em Streamlit que permite extrair dados de imagens PNG com base em campos como:

- **No. Serviço**
- **KM Final**
- **Total/Devido R$**

## 🛠️ Como usar

1. Faça o upload de imagens `.png` que contenham os dados estruturados conforme os modelos do MPRJ.
2. O app usará OCR para identificar os campos.
3. Baixe o resultado em formato Excel.

## ▶️ Executar localmente

### Requisitos

- Python 3.8+
- Tesseract OCR instalado no sistema:
  - **Windows**: https://github.com/UB-Mannheim/tesseract/wiki
  - **Linux**: `sudo apt install tesseract-ocr`
  - **MacOS**: `brew install tesseract`

### Passos

```bash
pip install -r requirements.txt
streamlit run app.py
```

## ☁️ Implantação no Streamlit Cloud

1. Suba este repositório no seu GitHub.
2. Vá para [https://streamlit.io/cloud](https://streamlit.io/cloud).
3. Conecte seu GitHub, escolha o repositório e arquivo `app.py`.
4. Clique em "Deploy".

---
