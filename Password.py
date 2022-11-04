from math import comb
for _ in range(int(input())):
    n = int(input())%10
    n %= 10
    n = 10 - n
    arr = list(map(int, input().split()))
    print(comb(4, 2) * (n*(n-1))//2)
