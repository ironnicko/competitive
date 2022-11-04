
for _ in range(int(input())):
    n = int(input())

    arr = list(map(int, input().split()))
    s = sum(arr)
    i = 1
    div = []
    while i <= n:
        if n % i == 0:
            div.append(i)
            if n//i != i:
                div.append(n//i)
        i += 1
        i *= i
    ans = n

    if len(div) <= 2:
        print(n)
    else:
        for i in div:
            req = s//i
            f = 0
            add = 0
            thi = 0
            mx = 0
            for j in range(n):
                add += arr[j]
                thi += 1
                if add == req:
                    mx = max(thi, mx)
                    add = 0
                    thi = 0
                elif s > req:
                    f = 1
                    break
        if not f:
            ans = min(ans, mx)
        print(ans)
