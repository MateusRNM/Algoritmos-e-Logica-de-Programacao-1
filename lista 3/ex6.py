n = int(input("Digite quantas pessoas deseja registrar: "))
soma_maiores_de_idade = 0
soma_menores_de_idade = 0
qtd_menores_de_idade = 0
for i in range(1, n+1):
    idade = int(input(f"Digite a idade da pessoa {i}: "))
    if idade >= 18:
        soma_maiores_de_idade += idade
    else:
        soma_menores_de_idade += idade
        qtd_menores_de_idade += 1
print(f"Soma da idade das pessoas maiores de idade: {soma_maiores_de_idade}")
print(f"Média de idade das pessoas menores de idade: {soma_menores_de_idade//qtd_menores_de_idade}" if qtd_menores_de_idade > 0 else "Nenhuma pessoa menor de idade informada")