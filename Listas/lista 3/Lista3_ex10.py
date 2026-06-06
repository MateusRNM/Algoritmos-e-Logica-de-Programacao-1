prime = [True] * 20001
for i in range(2, 142):
    if prime[i]:
        for j in range(i*i, 20001, i):
            prime[j] = False
for i in  range(2, 20001):
    if prime[i]:
        print(i)