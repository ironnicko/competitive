for _ in range(int(input())):
    n, l, r = map(int, input().split())
    f = 1
    for i in range(1, n+1):
        if r - (r%i) < l:
            f = 0
            break
    print("YES") if f else print("NO")
    if f:
        for i in range(1, n+1):
            print((r - (r % i)), end=" ")
        print()