for _ in range(int(input())):
    n, m, x = map(int, input().split())
    a = sorted(enumerate([int(i) for i in input().split()]), key=lambda x : x[1])
    ans = [1 for _ in range(n)]
    for i in range(n):
        ans[a[i][0]] = i % m  + 1
    print("YES")
    print(*ans)