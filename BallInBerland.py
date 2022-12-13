
from collections import defaultdict, deque, Counter
for _ in range(int(input())):
    A, B, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    ac = Counter(a)
    bc = Counter(b)
    sm = 0
    for i in range(k):
        sm += k - ac[a[i]] - bc[b[i]] + 1
    print(sm//2)
