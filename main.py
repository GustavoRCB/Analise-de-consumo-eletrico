from src.data_loader import carregar_dados
from src.analise import calcular_metricas
from src.visualizacao import grafico_linha

if __name__ == "__main__":
    caminho = "data/raw/consumo.csv"
    df = carregar_dados(caminho)

    metricas = calcular_metricas(df)

    print("\n=== MÉTRICAS DE CONSUMO ===")
    for chave, valor in metricas.items():
        print(f"{chave}: {valor:.2f}")

grafico_linha(df)