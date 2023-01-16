for _ in range(int(input())):
    input()
    x, y = set(), set()

    for _ in range(3):
        X, Y = map(int, input().split())
        x.add(X)
        y.add(Y)
    if len(set(x)) == 3:
        print("YES")
    elif len(set(y)) == 3:
        print("YES")
    else:
        print("NO")
