for _ in range(int(input())):
    n, k = map(int, input().split())
    a = 2*k-1-n
    x = list(range(1, k+1))
    x[a:] = x[a:][::-1]
    print(*x)
