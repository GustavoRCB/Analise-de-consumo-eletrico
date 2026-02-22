def calcular_metricas(df, tarifa=0.85):
    consumo_total = df["consumo_kwh"].sum()
    consumo_medio = df["consumo_kwh"].mean()
    pico_consumo = df["consumo_kwh"].max()
    custo_estimado = consumo_total * tarifa

    return {
        "consumo_total": consumo_total,
        "consumo_medio": consumo_medio,
        "pico_consumo": pico_consumo,
        "custo_estimado": custo_estimado
    }