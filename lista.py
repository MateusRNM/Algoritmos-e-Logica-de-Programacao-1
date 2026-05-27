numeros = []
soma = 0
for _ in range(10):
    numeros.append(int(input("Digite o numero: ")))
    soma += numeros[_]
print(f"A média das somas: {(soma/10):.10f}")