import streamlit as st
from src.data_loader import carregar_dados
from src.analise import calcular_metricas
import matplotlib.pyplot as plt

# Título
st.title("🔌 Dashboard de Consumo de Energia")

# Upload de arquivo
arquivo = st.file_uploader("Envie o arquivo CSV", type=["csv"])

if arquivo:
    df = carregar_dados(arquivo)

    # Mostrar dados
    st.subheader("📊 Dados Carregados")
    st.dataframe(df)

    # Calcular métricas
    metricas = calcular_metricas(df)

    st.subheader("📈 Métricas")
    col1, col2 = st.columns(2)

    col1.metric("Consumo Total (kWh)", f"{metricas['consumo_total']:.2f}")
    col1.metric("Consumo Médio (kWh)", f"{metricas['consumo_medio']:.2f}")

    col2.metric("Pico de Consumo (kWh)", f"{metricas['pico_consumo']:.2f}")
    col2.metric("Custo Estimado (R$)", f"{metricas['custo_estimado']:.2f}")

    # Gráfico
    st.subheader("📉 Consumo ao Longo do Tempo")

    fig, ax = plt.subplots()
    ax.plot(df["data"], df["consumo_kwh"])
    ax.set_xlabel("Data")
    ax.set_ylabel("Consumo (kWh)")
    ax.set_title("Consumo de Energia")
    plt.xticks(rotation=45)

    st.pyplot(fig)