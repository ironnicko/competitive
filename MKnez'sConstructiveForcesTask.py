
for _ in range(int(input())):
    n = int(input())
    if n == 3:
        print("NO")
    else:
        print("YES")
        if n & 1:
            a = n >> 1
            b = -(a-1)
            for _ in range(n):
                print((b, a)[_ & 1], end=" ")
        else:
            for _ in range(n):
                print((-1, 1)[_ & 1], end=" ")
        print()
