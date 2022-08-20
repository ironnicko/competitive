from math import sqrt, ceil
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x = int(input()) - 1

    ans = []
    while x >= 0:
        lower = ceil(sqrt(x))**2 - x
        ans.extend([i for i in range(lower, x+1)])
        x = lower-1

    print(*reversed(ans))
