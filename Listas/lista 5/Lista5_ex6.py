def calcularTempo(t):
    horas = t//3600
    t %= 3600
    minutos = t//60
    t %= 60
    print(f"O tempo de duração é de: {horas}h, {minutos}min e {t}s")

calcularTempo(5472)