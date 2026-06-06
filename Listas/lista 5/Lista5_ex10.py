soma_positivos = 0
qtd_positivos = 0
soma_negativos = 0
qtd_negativos = 0
for i in range(100):
    numero = int(input("Digite um número: "))
    if numero > 0:
        soma_positivos += numero
        qtd_positivos += 1
    elif numero < 0:
        soma_negativos += numero
        qtd_negativos += 1
print(f"Soma dos números positivos: {soma_positivos}")
print(f"Quantidade de números negativos: {qtd_negativos}")
print(f"Média dos números positivos: {soma_positivos / qtd_positivos if qtd_positivos > 0 else 0}")
print(f"Média dos números negativos: {soma_negativos / qtd_negativos if qtd_negativos > 0 else 0}")
print(f"Diferença entre o total de números positivos e negativos: {qtd_positivos - qtd_negativos}")