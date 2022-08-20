for _ in range(int(input())):
    n, H, M = map(int, input().split())
    s = d=  1440
    t1 = H * 60 + M
    for _ in range(n):
        h,m = map(int, input().split())
        t2 = h * 60 + m

        s =  min(s, (t2 - t1 + d) % d)
    print(s // 60, s % 60)