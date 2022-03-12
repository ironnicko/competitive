for _ in range(int(input())):
    n, m, r, c = map(int, input().split())
    a = [input().strip() for _ in range(n)]
    if a[r-1][c-1] == "B":
        print(0)
        continue
    if not any([x.count("B") != 0 for x in a]):
        print(-1)
        continue
    f = False
    for i in range(m):
        if a[r-1][i] == "B":
            f = True
    for i in range(n):
        if a[i][c-1] == "B":
            f = True
    if f:
        print(1)
    else:
        print(2)