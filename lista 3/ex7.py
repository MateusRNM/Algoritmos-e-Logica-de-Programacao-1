import math

n = int(input())
limit = math.ceil(n * (math.log(n) + math.log(math.log(n)))) + 5 if n >= 6 else 15
sum = 0
prime = [True] * (limit + 1)
prime[0] = prime[1] = False
limit_sqr = math.isqrt(limit)
for i in range(2, limit_sqr+1):
    if prime[i]:
        for j in range(i*i, limit+1, i):
            prime[j] = False
i = 2
while n:
    if prime[i]:
        sum += i
        n -= 1
    i += 1
print(sum)