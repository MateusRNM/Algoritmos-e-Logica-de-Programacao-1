def perfeito(n):
    soma = 0
    raizq = int(n**0.5)
    for i in range(1, raizq+1):
        if n%i == 0:
            soma += i
            if n/i != i and n/i != n:
                soma += n/i
    return 1 if soma == n else 0

n = int(input("Digite um número: "))
print(perfeito(n))