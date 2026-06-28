import pandas as pd


def calcular_metricas(df, tarifa=0.85):
    if df.empty:
        return {
            "consumo_total": 0,
            "consumo_medio": 0,
            "pico_consumo": 0,
            "demanda_maxima": 0,
            "fator_carga": 0,
            "custo_estimado": 0
        }

    consumo_total = df["consumo_kwh"].sum()
    consumo_medio = df["consumo_kwh"].mean()
    pico_consumo = df["consumo_kwh"].max()

    demanda_maxima = pico_consumo

    fator_carga = consumo_medio / demanda_maxima if demanda_maxima != 0 else 0

    custo_estimado = consumo_total * tarifa

    return {
        "consumo_total": consumo_total,
        "consumo_medio": consumo_medio,
        "pico_consumo": pico_consumo,
        "demanda_maxima": demanda_maxima,
        "fator_carga": fator_carga,
        "custo_estimado": custo_estimado
    }


def simular_tarifa_branca(df):
    if df.empty:
        return 0

    df_temp = df.copy()

    df_temp["hora"] = df_temp["data"].dt.hour

    def definir_tarifa(hora):
        if 18 <= hora < 21:
            return 1.20
        elif 17 <= hora < 18 or 21 <= hora < 22:
            return 0.85
        else:
            return 0.65

    df_temp["tarifa"] = df_temp["hora"].apply(definir_tarifa)

    custo_total = (df_temp["consumo_kwh"] * df_temp["tarifa"]).sum()

    return custo_total