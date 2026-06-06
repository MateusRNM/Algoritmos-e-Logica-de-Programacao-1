nums = []
for i in range(8):
    nums.append(int(input("Digite um número: ")))

for num in nums:
    if num%2 == 0:
        print(f"{num} é multiplo de 2")
    if num%3 == 0:
        print(f"{num} é multiplo de 3")