l1 = float(input("Digite o lado 1: "))
l2 = float(input("Digite o lado 2: "))
l3 = float(input("Digite o lado 3: "))
if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
   print("É um triângulo")
   if l1 == l2 and l3 == l1:
       print("Triângulo Equilátero")
   elif l1 != l2 and l3 != l2:
       print("Triângulo Escaleno")
   else:
       print("Triângulo Isósceles")
else:
   print("Não é um triângulo")