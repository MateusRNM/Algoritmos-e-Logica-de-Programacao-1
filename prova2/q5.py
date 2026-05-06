n = int(input("Digite o valor de N: "))
for i in range(1, n+1):
    line = ""
    for j in range(1, i+1):
        line += f"{j} "
    print(line)