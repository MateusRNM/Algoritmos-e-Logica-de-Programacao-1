funcionarios = ['Ana', 'Bruno', 'Carlos', 'Diana']
salarios = [1500.0, 3200.0, 1800.0, 4500.0]
for i in range(4):
    if salarios[i] <= 2000:
        salarios[i] *= 1.15
    else:
        salarios[i] *= 1.1
    print(f"Nome: {funcionarios[i]} - Novo Salário: R$ {salarios[i]}")