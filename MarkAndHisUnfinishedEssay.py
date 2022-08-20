for _ in range(int(input())):
    n, c, q = map(int, input().split())

    s = input()

    a =  [n]

    b = []

    for __ in range(c):
        l, r = map(int, input().split())
        a.append(a[-1] + r - l + 1)

        b.append((l, r))

    for ___ in range(q):
        k = int(input())
        x = c-1

        while x >= 0 and k > n:
            if k > a[x]:
                k += b[x][0] - a[x] -1 
            x -= 1
        print(s[k-1])