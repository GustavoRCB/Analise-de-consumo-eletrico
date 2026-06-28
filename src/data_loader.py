import pandas as pd


def carregar_dados(caminho):
    df = pd.read_csv(caminho)

    # Normalizar nomes das colunas
    df.columns = df.columns.str.lower().str.strip()

    # Detectar coluna de data automaticamente
    if "data" in df.columns:
        df["data"] = pd.to_datetime(df["data"])
    elif "data_hora" in df.columns:
        df["data"] = pd.to_datetime(df["data_hora"])
    elif "timestamp" in df.columns:
        df["data"] = pd.to_datetime(df["timestamp"])
    else:
        raise ValueError("Não foi encontrada coluna de data no CSV.")

    return df