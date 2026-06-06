nomes = []
medias = []
for i in range(5):
    nome = input("Digite o nome do aluno: ")
    media = float(input("Digite a média do aluno: "))
    nomes.append(nome)
    medias.append(media)
media_geral = sum(medias) / 5
acima_media = 0
for i in range(5):
    print(f"{nomes[i]} - Média: {medias[i]}")
    if medias[i] > media_geral:
        acima_media += 1
print(f"{acima_media} alunos ficaram acima da média geral.")