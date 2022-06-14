for _ in range(int(input())):
    n, B, x, y = map(int , input().split())
    ans, sum = 0, 0
    for i in range(n):
        if sum + x <= B:
            sum += x
        else:
            sum -= y
        ans += sum
    print(ans)
