for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = [0 for _ in range(n)]
    ans[0] = a[0]
    for i in range(1, n):
        prev = ans[i-1]
        if i != n -1:
            if a[i] != prev: ans[i] = a[i]
            elif b[i] != prev: ans[i] = b[i]
        else:
            next = ans[0]
            if a[i] != prev and a[i] != next: ans[i] = a[i]
            elif b[i] != prev and b[i] != next: ans[i] = b[i]
            elif c[i] != prev and c[i] != next: ans[i] = c[i]

    print(*ans)