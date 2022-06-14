for _ in range(int(input())):
    n, a = int(input()), [int(x) for x in input().split()]
    y = a.index(min(a))
    if n != 1:
        print(n if y else n - 1)
        for i in range(n):
            if i == y:
                continue
            print(i + 1, y + 1, a[y] + i, a[y])
        if y:
            print(1, y + 1, a[y], a[y] + y)
    else:
        print(0)