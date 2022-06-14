for _ in range(int(input())):
    n, m = map(int, input().split())
    a= sorted([int(i) for i in input().split()], reverse=1)
    ans = 0
    for i in range(m):
        ans += a[i+m] // a[i]
    print(ans + sum(a[2*m:]))