app.py
%%writefile app.py
import streamlit as st
import urllib

# 1. Cabeçalho Principal
st.set_page_config(page_title="Baccharis Bio Tech", page_icon="🌱", layout="wide")
st.title("🌱 Baccharis OS - Sistema Central")
st.subheader("Biorrefinaria e Gêmeo Digital (Conexão Japão ↔ Brasil)")
st.success("Status: Sensores de Hardware Conectados e Operantes!")

# 2. Painel de Interação e Mensagens
st.divider() # Cria uma linha divisória na tela
st.header("📡 Comunicação Global")

nome_socio = st.text_input("Qual o seu nome?")
mensagem = st.text_input("Digite uma mensagem para a equipe:")

# Criando o primeiro botão
if st.button("Enviar Mensagem"):
    st.info(f"O sócio **{nome_socio}** enviou: {mensagem}")

# 3. Painel de Controle de Hardware (Gêmeo Digital)
st.divider()
st.header("🏭 Controle da Torre 1 (Máquina)")

# Organizando os botões em duas colunas para ficar bonito
col1, col2 = st.columns(2)

with col1:
    # Botão de Ligar a Máquina
    if st.button("🔥 Ligar Secador Térmico"):
        st.warning("ALERTA: Secador Térmico ativado! Temperatura subindo para 60°C.")

with col2:
    # Botão de Extração
    if st.button("💧 Iniciar Extração de Artepilin C"):
        st.balloons() # Um efeito visual divertido do Streamlit
        st.success("Extração iniciada com sucesso! Válvulas abertas.")

# 4. Senha de Segurança no rodapé
st.divider()
senha_ip = urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip()
st.caption(f"🔒 Chave de Segurança da Sessão: {senha_ip}")
