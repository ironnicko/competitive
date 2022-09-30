for _ in range(int(input())):
    n,m = map(int, input().split())

    a = sorted([int(i) for i in input().split()])

    c = 1
    ans = 0
    for i in range(n-1, -1, -1):
        if not(c * a[i] < m):
            ans += 1
            c = 1
        else:
            c+=1

    print(ans)