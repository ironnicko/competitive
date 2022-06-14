from bisect import bisect_left
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n, m = map(int, input().rstrip().split())
    a = sorted([int(i) for i in input().rstrip().split()], reverse=1)
    for i in range(1, n):
        a[i] = a[i] + a[i-1]
    for _ in range(m):
        k = int(input())
        left = bisect_left(a, k)+1
        print("-1\n") if left > n else print(str(left)+"\n")
    