def bs_sqrt(n):
    l = 0
    r = 1000000000000000001
    while r > l:
        mid = l + ((r -l)//2)
        if (mid * mid) > n:
            r = mid
        else:
            l = mid + 1
    return l- 1


for _ in range(int(input())):

    l, r = map(int, input().split())
    l_r = int(bs_sqrt(l))
    r_r = int(bs_sqrt(r))

    if l_r == r_r:
        ans = 0
        for i in range(3):
            if l <= l_r * (l_r + i) and l_r * (l_r + i) <= r:
                ans += 1

    else:
        ans = (r_r - l_r - 1) * 3
        for i in range(3):
            if l <= (l_r * (l_r + i)) and (l_r * (l_r + i)) <= r:
                ans += 1
            if l <= (r_r * (r_r + i)) and (r_r * (r_r + i)) <= r:
                ans += 1
    print(ans)