from collections import defaultdict

q = int(input())
h = defaultdict(int)
S = {0, }
for _ in range(q):
    t, n = input().split()
    n = int(n)

    if t == '+':
        S.add(n)
    else:
        t = (n, h[n])[n in h]
        while t in S:
            t += n
        h[n] = t
        print(t)
