from bisect import bisect_left, bisect_right
from collections import defaultdict

# sieve
N = 1001
sieve = [1 for _ in range(N)]
primes = []
for i in range(2, N):
    j = i
    while i * j < N:
        sieve[i*j] = 0
        j += 1
    if sieve[i]:
        primes.append(i)


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    sP = defaultdict(list)
    colors = [-1 for _ in range(n)]
    vis = {}
    counter = 0
    for x, i in enumerate(arr):
        for k in range(len(primes)):
            if not (i % primes[k]) and i not in sP[primes[k]]:
                if primes[k] not in vis:
                    counter += 1
                    vis[primes[k]] = counter
                colors[x] = vis[primes[k]]
                break

    print(len(vis))
    print(*colors)
