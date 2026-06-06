soma_notas = float(input())
soma_notas += float(input())
soma_notas += float(input())
media = soma_notas/3
print(media)
if media >= 7:
   print("Aprovado")
elif media >= 3:
  print("Exame")
  print(f"Nota mínima: {6 - media}")
else:
  print("Reprovado")