
from collections import deque
MOD = int(1e9 + 1)
for _ in range(int(input())):
    n = int(input())
    arr = deque(map(int, input().split()))
    f = arr.popleft()
    arr = sorted(arr)
    for i in range(n-1):
        if f < arr[i]:
            f += (arr[i] - f + 1) >> 1
    print(f)
