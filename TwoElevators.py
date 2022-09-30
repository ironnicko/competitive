for _ in range(int(input())):
    n, x, y = map(int, input().split())
    floor = abs(x-y)
    second = y - 1
    d = floor + second
    e = n -1 
    if d > e: print(1)
    elif d < e: print(2)
    else: print(3)