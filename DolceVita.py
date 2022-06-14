for _ in range(int(input())):
    n, x = map(int, input().split())
    a =sorted([int(i) for i in input().split()])
    ans = 0
    for i in range(n):
        if x >=a[i]:
            ans += (x-a[i])//(i+1) + 1
        x -= a[i]
    print(ans)