import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    d = [[] for i in range(n)]
    w = []
    for i in range(n):
        a, b = map(int, input().split())
        w.append([a-1, b-1])
        d[a-1].append(i)
        d[b-1].append(i)

    if max(len(i) for i in d) > 2:
        print('NO')
        continue

    q = [0]*n
    for i in range(n):
        if q[i] == 0:
            q[i] = 1
            x, y = w[i]
            c = 1
            while x != y:
                i = sum(d[x]) - i
                x = sum(w[i]) - x
                q[i] = 1
                c += 1
            if c % 2:
                print('NO')
                break
    else:
        print('YES')