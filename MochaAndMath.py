for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    ans = a[0]
    for i in a:
        ans = min(ans, i & ans)
    print(ans)