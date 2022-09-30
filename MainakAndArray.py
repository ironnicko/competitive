for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    if len(a) == 1:
        print(0)
        continue

    ans = 0

    for i in range(n-1):
        ans = max(ans, a[i] - a[i+1])
    for i in range(n-1):
        ans = max(ans, a[-1] - a[i])
    for i in range(1, n):
        ans = max(ans, a[i] - a[0])
    
    print(ans)