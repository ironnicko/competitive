# learnning python
for _ in range(int(input())):
    a,s=map(int,input().split())
    b = 0
    bdeg = 1
    while s > 0:
        s0, a0 = s%10, a%10
        if s0 >= a0:
            b += bdeg * (s0-a0)
            s //= 10
        elif s%100 - a0 in range(10):
            b += bdeg * (s%100 - a0)
            s //= 100
        else:
            break
        a //= 10
        bdeg *= 10
    print (-1 if s>0 or a>0 else b)