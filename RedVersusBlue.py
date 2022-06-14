
for _ in range(int(input())):
    n, r, b = map(int, input().split())

    dd, mm = divmod(r, b+1)

    s = ''

    for i in range(b):
        s += 'R' * dd
        if i < mm:
            s += 'R'
        s += 'B'

    s += 'R' * dd

    print(s)
