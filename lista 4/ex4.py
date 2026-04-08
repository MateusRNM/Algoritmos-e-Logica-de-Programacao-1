def baskara(a, b, c):
    delta = b*b -4 * a * c
    if delta < 0:
        print("Não existe raiz para essa equação no conjunto dos números reais.")
    elif delta == 0:
        print(f"A raiz dessa equação é: {-b/(2*a)}")
    else:
        print(f"As raízes dessa equação são: {(-b+(delta**0.5))/(2*a)} e {(-b-(delta**0.5))/(2*a)}")