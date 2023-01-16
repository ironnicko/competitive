from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = deque()
    for i in range(n//2):
        arr.extend((n-i, i+1))
    if n & 1:
        arr.append((n>>1) + 1)
    print(*arr)
