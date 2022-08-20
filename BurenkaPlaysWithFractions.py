MOD = 1e13
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())

    if a * d == b *c:
        print(0%int(MOD))
    else:
        P1 = a * d
        P2 = b * c
        if P2 != 0 and P1 % P2 ==0:
            print(1)
        elif P1 != 0 and P2 % P1 ==0:
            print(1)
        else:
            print(2)