from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    k = 0
    for j in range(1, n):
        k = gcd(k, a[j]-a[j-1])

    if k == 0:
        print(-1)
    else:
        print(k)
