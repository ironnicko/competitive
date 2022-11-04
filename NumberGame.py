import sys
import random
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = [int(xx) for xx in input().split()]
    a = sorted(a)
    for k in range((n + 1) // 2, -1, -1):
        q = []
        for i in range(k - 1, k - 1 + k):
            if a[i] > i - k + 2:
                break
        else:
            print(k)
            break
    else:
        print(0)