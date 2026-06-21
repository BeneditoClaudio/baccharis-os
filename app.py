import streamlit as st

# Configuração da página
st.set_page_config(page_title="Baccharis OS - Digital Twin", layout="wide")

# Seletor de Idioma
lang = st.sidebar.selectbox("Language / Idioma / 言語", ["Português", "English", "日本語"])

# Dicionário de textos
texts = {
    "Português": {"title": "Baccharis OS - Sistema Central", "tab1": "Painel Biorrefinaria", "tab2": "Vídeo Institucional", "tab3": "Inventário WS Maps", "contact": "Contato"},
    "English": {"title": "Baccharis OS - Central System", "tab1": "Biorefinery Panel", "tab2": "Institutional Video", "tab3": "WS Maps Inventory", "contact": "Contact"},
    "日本語": {"title": "Baccharis OS - 中央システム", "tab1": "バイオリファイナリーパネル", "tab2": "紹介動画", "tab3": "WS Maps インベントリ", "contact": "連絡先"}
}

t = texts[lang]

# Título Principal
st.title(f"🌍 {t['title']}")

# Barra Lateral: Cartão de Visita
with st.sidebar:
    st.image("cartao_baccharis.png", use_container_width=True) # Certifique-se que o nome do arquivo está exato!
    st.subheader(t['contact'])
    st.write("dosu.santosu@baccharisbio.com")

# Abas Principais
tab1, tab2, tab3 = st.tabs([t['tab1'], t['tab2'], t['tab3']])

with tab1:
    st.header(t['tab1'])
    st.write("Monitoramento de torres e processos em tempo real.")
    # Aqui entra a lógica das torres que criamos no Colab

with tab2:
    st.header(t['tab2'])
    # Substitua a URL pela do vídeo oficial do Sítio Família Santos
    st.video("https://www.youtube.com/watch?v=SEU_LINK_AQUI")

with tab3:
    st.header(t['tab3'])
    st.write("Dados do inventário WS Maps.")
    # Aqui você pode carregar seu CSV ou dados do inventário
