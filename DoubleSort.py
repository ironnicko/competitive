from sys import stdin,stdout
from collections import Counter
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    f=1
    a = [int(i) for i in input().rstrip().split()]
    b = [int(i) for i in input().rstrip().split()]
    c = []
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[j] <= a[i] and b[j] <= b[i] and (a[i] != a[j] or b[i] != b[j]):
                a[i], a[j] = a[j], a[i]
                b[i], b[j] = b[j], b[i]
                c.append(sorted((i+1, j+1)))
                count += 1
    for i in range(n-1):
        if not(a[i]<=a[i+1] and b[i]<=b[i+1]):
            print("-1\n")
            break
    else:
        print(f"{count}\n")
        for i in c:
            print(f"{i[0]} {i[1]}\n")
