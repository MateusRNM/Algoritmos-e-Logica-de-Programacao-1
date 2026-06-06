soma_notas = float(input())
soma_notas += float(input())
soma_notas += float(input())
media = soma_notas/3
print(media)
if media >= 8:
   print("A")
elif media >= 7:
  print("B")
elif media >= 6:
  print("C")
elif media >= 5:
  print("D")
else:
  print("E")