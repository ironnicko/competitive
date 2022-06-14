for _ in range(int(input())):
    n, m = map(int, input().split())
    if n == 1 or m == 1:
        if n + m > 3:
            print(-1)
            continue
    maxi = (max(n,m) - 1) * 2
    maxi -= 1 if n%2 != m%2 else 0 
    print(maxi)