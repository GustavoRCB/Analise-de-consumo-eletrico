import streamlit as st
import pandas as pd
from src.data_loader import carregar_dados
from src.analise import calcular_metricas, simular_tarifa_branca
from src.visualizacao import grafico_linha

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Dashboard de Energia",
    page_icon="⚡",
    layout="wide"
)

st.title(" Dashboard de Consumo de Energia")

# =========================
# UPLOAD DO CSV
# =========================
uploaded_file = st.file_uploader(
    " Envie seu arquivo CSV de consumo",
    type=["csv"]
)

if uploaded_file is not None:
    df = carregar_dados(uploaded_file)
else:
    st.info("Usando arquivo padrão (data/raw/consumo.csv)")
    caminho = "data/raw/consumo.csv"
    df = carregar_dados(caminho)

# Garantir datetime
df["data"] = pd.to_datetime(df["data"])

# =========================
# SIDEBAR - FILTROS
# =========================
st.sidebar.header(" Filtro de Período")

data_inicio = st.sidebar.date_input("Data inicial", df["data"].min())
data_fim = st.sidebar.date_input("Data final", df["data"].max())

df_filtrado = df[
    (df["data"] >= pd.to_datetime(data_inicio)) &
    (df["data"] <= pd.to_datetime(data_fim))
].copy()

# =========================
# SIDEBAR - TARIFA SIMPLES
# =========================
st.sidebar.header(" Simulação de Tarifa")

tarifa = st.sidebar.number_input(
    "Valor da tarifa (R$/kWh)",
    min_value=0.0,
    value=0.85,
    step=0.05
)

# =========================
# MÉTRICAS
# =========================
metricas = calcular_metricas(df_filtrado, tarifa=tarifa)

fator = metricas["fator_carga"]

if fator >= 0.75:
    classificacao = "🟢 Perfil eficiente"
elif fator >= 0.50:
    classificacao = "🟡 Perfil moderado"
else:
    classificacao = "🔴 Baixo fator de carga"

st.subheader(" Métricas Elétricas")

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

col1.metric("Consumo Total", f"{metricas['consumo_total']:.2f} kWh")
col2.metric("Consumo Médio", f"{metricas['consumo_medio']:.2f} kWh")
col3.metric("Pico de Consumo", f"{metricas['pico_consumo']:.2f} kWh")

col4.metric("Demanda Máxima", f"{metricas['demanda_maxima']:.2f} kWh")
col5.metric("Fator de Carga", f"{metricas['fator_carga']:.2f}")
col6.metric("Custo Estimado", f"R$ {metricas['custo_estimado']:.2f}")

st.info(f"Classificação do Perfil: {classificacao}")

# =========================
# TARIFA BRANCA
# =========================
st.subheader(" Simulação Tarifa Branca")

custo_branca = simular_tarifa_branca(df_filtrado)

col7, col8 = st.columns(2)

col7.metric("Custo Tarifa Convencional", f"R$ {metricas['custo_estimado']:.2f}")
col8.metric("Custo Tarifa Branca", f"R$ {custo_branca:.2f}")

# =========================
# MÉDIA MÓVEL
# =========================
df_filtrado["media_movel"] = df_filtrado["consumo_kwh"].rolling(24).mean()

st.subheader(" Tendência de Consumo (Média Móvel)")

st.line_chart(
    df_filtrado.set_index("data")[["consumo_kwh", "media_movel"]]
)

# =========================
# GRÁFICOS
# =========================
st.subheader(" Evolução do Consumo")
grafico_linha(df_filtrado)

st.subheader(" Dados Filtrados")
st.dataframe(df_filtrado)