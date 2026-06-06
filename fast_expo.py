base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
a = base
b = expoente
res = 1
while(b > 0):
    if(b & 1):
        res *= a
    a *= a
    b //= 2
print(f"{base}^{expoente} = {res}") 