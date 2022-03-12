for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    ib, ir = 1, n-1
    sb, sr = a[0] + a[1], a[n-1]
    while ib <= ir and sb >= sr:
        ib += 1
        ir -= 1
        sb += a[ib]
        sr += a[ir]
    print('YES' if ir >= ib else 'NO')