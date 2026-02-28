import streamlit as st
from src.data_loader import carregar_dados
from src.analise import calcular_metricas
from src.visualizacao import grafico_linha

# Caminho do arquivo
caminho = "data/raw/consumo.csv"

# Carrega dados
df = carregar_dados(caminho)

# Calcula métricas
metricas = calcular_metricas(df)

# ===== DASHBOARD =====

st.title("📊 Dashboard de Consumo de Energia")

st.subheader("📈 Gráfico de Consumo")
grafico_linha(df)  # precisa usar st dentro dessa função

st.subheader("📊 Métricas")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Consumo Total", f"{metricas['consumo_total']:.2f} kWh")
col2.metric("Consumo Médio", f"{metricas['consumo_medio']:.2f} kWh")
col3.metric("Pico de Consumo", f"{metricas['pico_consumo']:.2f} kWh")
col4.metric("Custo Estimado", f"R$ {metricas['custo_estimado']:.2f}")