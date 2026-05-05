l1 = float(input("Digite o lado 1: "))
l2 = float(input("Digite o lado 2: "))
l3 = float(input("Digite o lado 3: "))
ang = float(input("Digite o maior ângulo: "))
if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
    if l1 == l2 and l2 == l3:
        print("É equilátero.")
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print("É isósceles.")
    else:
        print("É escaleno")
    
    if ang == 90:
        print("É retângulo")
    elif ang > 90:
        print("É obtusângulo")
    else:
        print("É Acutângulo")
else:
    print("Medidas inválidas")