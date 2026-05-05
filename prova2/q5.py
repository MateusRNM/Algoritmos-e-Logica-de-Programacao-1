n = int(input("Digite o valor de N: "))
for i in range(n, -1, -1):
    line = ""
    for j in range(1, n-i+1):
        line += f"{j} "
    print(line)