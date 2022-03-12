for _ in range(int(input())):
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    diff = a[-1]-sum(a[:-1])
    if not(a[-1]):
        print(0)
    elif diff <= 1:
        print(1)
    else:
        print(diff)