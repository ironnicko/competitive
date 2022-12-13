for _ in range(int(input()) % int(1e5)):
    l, r, x = map(int, input().split())

    a,b = map(int, input().split())

    first,second,third,fourth = abs(l-a) < x, abs(r-a) < x, abs(l-b) < x, abs(r-b) < x

    cond =(first and second) or (third  and fourth)
    if a == b:
        print(0)
    elif abs(b-a) >= x:
        print(1)
    elif cond:
        print(-1)
    else:
        if first:
            ans = 2 + int(fourth)
        elif second:
            ans = 2 + int(third)
        else:
            ans = 2
        print(ans)

