precos = [1.3, 2.6, 12]
bilhete = -1
while bilhete < 0 or bilhete > 2:
   bilhete = int(input("Digite qual o tipo de bilhete (0 - Unitário, 1 - Duplo, 2 - 10 viagens) "))
valor = float(input("Digite o valor pago: "))
print(f"Você comprou {int(valor//precos[bilhete])} e seu troco é de {valor - valor//precos[bilhete] * precos[bilhete]}")