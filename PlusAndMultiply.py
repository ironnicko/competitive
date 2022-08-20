for _ in range(int(input())):
    n, a, b = map(int, input().split())
    if a==1:
        print(("No", "Yes")[int((n-1)%b == 0)])
    else:
        t = 1
        f = 0
        while t <= n:
            if t%b == n%b:
                f=1
                break
            t *= a

        print(("No", "Yes")[f])