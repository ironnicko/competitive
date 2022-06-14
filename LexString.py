from collections import deque
from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print =lambda x : stdout.write(str(x)+"\n")

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = sorted(deque([i for i in input()]))
    b = sorted(deque([i for i in input()]))

    i  = 0
    j = 0
    h  = k
    g = k
    res = ""

    while i < n and j < m:
        if (h == 0):
                res += b[j]
                h = k
                g-=1
                j+=1
                continue

        if (g == 0):
            res += a[i]
            g = k
            h-=1
            i+=1
            continue
        if (a[i] <= b[j]):

            res += a[i]
            i+=1
            h-=1
            g = k
        else:
            res += b[j]
            j+=1
            g-=1
            h = k
    print(res)