produtos = []
while True:
    preco = float(input("Digite o valor do produto (ou um valor negativo para finalizar): "))
    if preco < 0:
        break
    produtos.append(preco)
valor_total = sum(produtos)
desconto = valor_total * (0.05 if len(produtos) > 10 else 0)
print(f"{len(produtos)} produtos comprados:\nValor Bruto: {valor_total}\nDesconto Calculado: {desconto}\nValor Final: {valor_total - desconto}")