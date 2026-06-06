votos = [1, 2, 3, 3, 2, 1, 1, 2, 3, 2, 2, 1, 3, 2, 1, 1, 2, 3, 2, 1]
votos_ruim = votos.count(1)
votos_bom = votos.count(2)
votos_excelente = votos.count(3)
print(f"Votos Ruins: {votos_ruim} ({(votos_ruim/len(votos) * 100):.2f}%)")
print(f"Votos Bons: {votos_bom} ({(votos_bom/len(votos) * 100):.2f}%)")
print(f"Votos Excelentes: {votos_excelente} ({(votos_excelente/len(votos) * 100):.2f}%)")
if votos_ruim > votos_bom and votos_ruim > votos_excelente:
    print("A avaliação vencedora foi a Ruim")
elif votos_bom > votos_ruim and votos_bom > votos_excelente:
    print("A avaliação vencedora foi a Boa")
elif votos_excelente > votos_ruim and votos_excelente > votos_bom:
    print("A avaliação vencedora foi a Excelente")
else:
    print("Empate nas avaliações")
