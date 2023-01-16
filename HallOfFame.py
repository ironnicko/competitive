
for _ in range(int(input())):
    n = int(input())
    s = input()
    ls = s.count('L')
    rs = n - ls

    if not rs or not ls:
        print(-1)
    else:
        ans = 0
        for i in range(n-1):
            if s[i] + s[i+1] == "LR":
                ans = i+1
                break
        print(ans)
