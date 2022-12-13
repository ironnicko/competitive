for _ in range(int(input())):
    n = int(input()) % int(1e5+1)
    if n & 1:
        print(*[n for _ in range(n)])
    else:
        for i in range(n-2):
            print(2, end=" ")
        print(1, 3)
    