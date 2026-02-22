import pandas as pd

def carregar_dados(caminho):
    df = pd.read_csv(caminho, parse_dates=["data"])
    df["consumo_kwh"] = df["consumo_kwh"].astype(float)
    return df