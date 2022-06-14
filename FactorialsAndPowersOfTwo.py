from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print = stdout.write

from math import factorial
from itertools import combinations

for _ in range(int(input())):
    facts = []
    for i in range(3, 15):
        facts.append(factorial(i))

    combs = []
    for i in range(15):
        for j in combinations(facts, i):
            combs.append([len(j), sum(j)])

    x = int(input())
    res = []
    for i, k in combs:
        if (x - k) >= 0:
            b = bin(x - k)
            res.append(i + b.count('1'))

    print(f"{min(res)}\n")