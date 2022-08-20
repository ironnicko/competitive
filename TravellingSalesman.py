

for _ in range(int(input())):
    n = int(input())
    X, x, y, Y = (0 for _ in range(4))
    for _ in range(n):
        a ,b = map(int, input().split())
        X = max(X, a)
        x = min(x, a)

        Y = max(Y, b)
        y = min(y, b)
    score = 2 * (Y - y + X - x)
    print(score)