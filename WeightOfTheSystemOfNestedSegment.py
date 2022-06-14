t = int(input())
for _ in range(t):
    s = input()
    n, m = map(int, input().split())
    a = []
    for i in range(m):
        x, w = map(int, input().split())
        a.append([w, x, i+1])
    a.sort()
    a = a[:2*n]
    a.sort(key=lambda x: x[1])
    sm = 0
    for i in range(len(a)):
        sm += a[i][0]
    print(sm)
    for i in range(len(a) // 2):
        print(a[i][2], a[-i-1][2])
    print()
