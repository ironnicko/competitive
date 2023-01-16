
for _ in range(int(input())):
    w, d, h = map(int, input().split())

    a, b, f, g = map(int, input().split())

    h += min((abs(a - f) + min(b + g, d - b + d - g)),
             (abs(b - g) + min(a + f, w - f + w - a)))
    print(h)
