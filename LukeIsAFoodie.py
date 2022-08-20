for _ in range(int(input())):
    n, x = map(int, input().split())
    a = [int(i) for i in input().split()]
    mini = a[0]
    maxi = a[0]
    cnt = 0
    for i in a:
        mini = min(mini, i)
        maxi = max(maxi, i)
        if maxi - mini > 2 * x:
            maxi, mini = i, i
            cnt += 1
    print(cnt)