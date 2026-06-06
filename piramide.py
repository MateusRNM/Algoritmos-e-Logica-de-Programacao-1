def piramide(n):
    for i in range(0, n):
        print(f"{" " * (n-i-1) + "*" * (2*i+1)}")
piramide(int(input()))