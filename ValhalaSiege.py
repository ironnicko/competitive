from bisect import bisect_right
from sys import stdin, stdout
input = stdin.readline
print = stdout.write

n,q = map(int, input().rstrip().split())
a = [int(i) for i in input().rstrip().split()]
b = [int(i) for i in input().rstrip().split()]
for i in range(1, n):
    a[i] += a[i-1]
c = 0
for i in b:
    c += i
    t = bisect_right(a, c)
    if n != t:
        print(f"{n-t}\n")
    else:
        print(f"{n}\n")
        c =0