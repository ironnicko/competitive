from math import log
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(n)
    for i, x in enumerate(arr):
        it = int(x)
        while it & (it-1):
            it += 1
        print(i+1, it - x)
