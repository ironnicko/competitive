for _ in range(int(input())):
    n, m = map(int, input().split())

    n = abs(n)
    m = abs(m)

    add = n + m
    diff = abs(n - m)

    if n == m:
        print(add)
    else:
        print(add + diff - 1)