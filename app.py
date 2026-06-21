import streamlit as st

# Configuração da página
st.set_page_config(page_title="Baccharis OS - Digital Twin", layout="wide")

# Seletor de Idioma
lang = st.sidebar.selectbox("Language / Idioma / 言語", ["Português", "English", "日本語"])

# Dicionário de textos
texts = {
    "Português": {"title": "Baccharis OS - Sistema Central", "tab1": "Painel Biorrefinaria", "tab2": "Vídeo Institucional", "tab3": "Inventário WS Maps"},
    "English": {"title": "Baccharis OS - Central System", "tab1": "Biorefinery Panel", "tab2": "Institutional Video", "tab3": "WS Maps Inventory"},
    "日本語": {"title": "Baccharis OS - 中央システム", "tab1": "バイオリファイナリーパネル", "tab2": "紹介動画", "tab3": "WS Maps インベントリ"}
}

t = texts[lang]
st.title(f"🌍 {t['title']}")

# Abas Principais
tab1, tab2, tab3 = st.tabs([t['tab1'], t['tab2'], t['tab3']])

with tab1:
    st.write("Monitoramento em tempo real da Biorrefinaria...")

with tab2:
    st.header(t['tab2'])
    # Inserindo o seu vídeo aqui:
    st.video("https://youtu.be/lmrCoiHifbo")

with tab3:
    st.write("Dados de inventário em carregamento...")
