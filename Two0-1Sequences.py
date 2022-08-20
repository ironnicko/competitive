for _ in range(int(input())):
    n, m = map(int, input().split())

    a = input()
    b = input()

    print(("NO", "YES")[a[n-m+1:] == b[1:] and b[0] in a[:n-m+1]])