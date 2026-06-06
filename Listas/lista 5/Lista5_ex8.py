salario_2filhos = 0
salario_sem_filhos = 0
salario_geral = 0
qtde_2filhos = 0
qtde_sem_filhos = 0
qtde_geral = 0
for i in range(100):
    input("Digite seu nome: ")
    salario = float(input("Digite seu salário: "))
    filhos = int(input("Digite a quantidade de filhos: "))
    if filhos == 2:
        salario_2filhos += salario
        qtde_2filhos += 1
    elif filhos == 0:
        salario_sem_filhos += salario
        qtde_sem_filhos += 1
    salario_geral += salario
    qtde_geral += 1

media_2filhos = salario_2filhos / (qtde_2filhos if qtde_2filhos > 0 else 1)
media_sem_filhos = salario_sem_filhos / (qtde_sem_filhos if qtde_sem_filhos > 0 else 1)
media_geral = salario_geral / (qtde_geral if qtde_geral > 0 else 1)
print(f"Média salarial das pessoas com 2 filhos: {media_2filhos}")
print(f"Média salarial das pessoas sem filhos: {media_sem_filhos}")
print(f"A média salarial geral das pessoas com 2 filhos é {'menor do que' if media_2filhos < media_sem_filhos else ('igual' if media_2filhos == media_sem_filhos else 'maior do que')} a média salarial geral das pessoas sem filhos.")
print(f"Média salarial geral: {media_geral}")