import matplotlib.pyplot as plt

def grafico_linha(df):
    plt.figure()
    plt.plot(df["data"], df["consumo_kwh"])
    plt.xlabel("Data")
    plt.ylabel("Consumo (kWh)")
    plt.title("Consumo de Energia ao Longo do Tempo")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()