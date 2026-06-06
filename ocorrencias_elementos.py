import time

def limite_superior(a, target):
    l, r = 0, len(a)-1
    ans = -1
    while l <= r:
        m = l+(r-l)//2
        if a[m] == target:
            ans = m
            l = m + 1
        elif a[m] < target:
            l = m + 1
        else:
            r = m - 1
    return ans

def limite_inferior(a, target):
    l, r = 0, len(a)-1
    ans = -1
    while l <= r:
        m = l+(r-l)//2
        if a[m] == target:
            ans = m
            r = m - 1
        elif a[m] < target:
            l = m + 1
        else:
            r = m - 1
    return ans

def calcular_ocorrencias(a, target):
    a.sort()
    inf = limite_inferior(a, target)
    if inf == -1:
        return 0
    else:
        sup = limite_superior(a, target)
        return sup-inf+1

def busca_linear(a, target):
    counter = 0
    for num in a:
        if num == target:
            counter += 1
    return counter

a = [0, 0, 2, 3, 5, 1, 1, 0, 0, 20]

inicio = time.perf_counter()
res_bl = busca_linear(a, 0)
fim = time.perf_counter()
print(f"Busca linear:\nResultado: {res_bl}\nTempo de execução: {fim - inicio:.6f} segundos")

inicio = time.perf_counter()
res_bb = calcular_ocorrencias(a, 0)
fim = time.perf_counter()
print(f"Busca binária:\nResultado: {res_bb}\nTempo de execução: {fim - inicio:.6f} segundos")