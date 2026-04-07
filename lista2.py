# 1 - num = int(input())
# num = min(num, int(input()))
# print(num)

# 2 - num = int(input())
# num = min(num, int(input()))
# num = min(num, int(input()))
# print(num)

# 3 - num = int(input())
# num = min(num, int(input()))
# num = min(num, int(input()))
# num = min(num, int(input()))
# print(num)

# 4 - num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# if num1 > num3:
#   num1 = num3
# elif num2 > num3:
#   num2 = num3
# print(num1)
# print(num2)

# 5 -
#qtd_maior_100 = 0
#for i in range(0, 5):
#    if int(input()) > 100:
#        qtd_maior_100 += 1
#print(qtd_maior_100)

# 6 -
# valor = int(input())
# if valor > 10:
#   print("É MAIOR QUE 10")
# else:
#    print("NÃO É MAIOR QUE 10")

# 7 -
# if int(input()) & 1:
#   print("É ÍMPAR")
# else:
#   print("É PAR")

# 8 -
# if 2026-int(input()) >= 16:
#   print("Pode votar")
# else:
#   print("Não pode votar")

# 9 -
# idade = int(input())
# peso = float(input())
# if idade >= 18 and idade <= 69 and peso >= 50:
#   print("Pode doar sangue")
# else:
#    print("Não pode doar sangue")

# 10 - 
# sexo = input("Você é do sexo masculino? (y/n)")
# idade = int(input("Qual sua idade? "))
# if sexo == y and idade >= 18:
#   print("Bem-vindo ao exército!")

# 11 -
#num = int(input())
#if not (num & 1):
#    print(num*num)

# 12 -
#qtd = 0
#for i in range(0, 5):
#    num = int(input())
#    if num < 17 and num > 10:
#        qtd += 1
#print(qtd)

# 13 - 
#qtd1 = 0
#qtd2 = 0
#qtd3 = 0
#for i in range(0, 5):
#    num = int(input())
#    if num > 100:
#        qtd1 += 1
#    elif num < 17:
#        qtd2 += 1
#    else:
#        qtd3 += 1
#print(qtd1)
#print(qtd2)
#print(qtd3)

# 14 -
# soma_notas = float(input())
# soma_notas += float(input())
# soma_notas += float(input())
# media = soma_notas/3
# print(media)
# if media >= 8:
#    print("A")
# elif media >= 7:
#   print("B")
# elif media >= 6:
#   print("C")
# elif media >= 5:
#   print("D")
# else:
#   print("E")

# 15 - 
# soma_notas = float(input())
# soma_notas += float(input())
# soma_notas += float(input())
# media = soma_notas/3
# print(media)
# if media >= 7:
#    print("Aprovado")
# elif media >= 3:
#   print("Exame")
#   print(f"Nota mínima: {6 - media}")
# else:
#   print("Reprovado")

# 16 -
# precos = [1.3, 2.6, 12]
# bilhete = -1
# while bilhete < 0 or bilhete > 2:
#    bilhete = int(input("Digite qual o tipo de bilhete (0 - Unitário, 1 - Duplo, 2 - 10 viagens) "))
# valor = float(input("Digite o valor pago: "))
# print(f"Você comprou {int(valor//precos[bilhete])} e seu troco é de {valor - valor//precos[bilhete] * precos[bilhete]}")

# 17 - 
#l1 = float(input("Digite o lado 1: "))
#l2 = float(input("Digite o lado 2: "))
#l3 = float(input("Digite o lado 3: "))
#if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
#    print("É um triângulo")
#    if l1 == l2 and l3 == l1:
#        print("Triângulo Equilátero")
#    elif l1 != l2 and l3 != l2:
#        print("Triângulo Escaleno")
#    else:
#        print("Triângulo Isósceles")
#else:
#    print("Não é um triângulo")