total_livros = 0
fiction = 0
for i in range(6):
    input("Digite seu nome: ")
    total_livros += int(input("Digite a quantidade de livros que você leu esse ano: "))
    fiction += 1 if int(input("Digite seu genêro favorito dentre: 0 - Ficcção, 1 - Não-Ficção ")) == 0 else 0
print(f"O total de livros lido pelo grupo foi de {total_livros}")
print(f"A porcentagem de pessoas que preferem ficcção é: {fiction/6 * 100}%")
print(f"A porcentagem de pessoas que preferem não-ficcção é: {(6-fiction)/6 * 100}%")
