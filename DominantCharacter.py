for _ in range(int(input())):
    n = int(input())
    s = input()
    c = 0
    ans = []
    for i in range(n):
        if s[i] == 'a':
            if i+1 < n and s[i+1] == 'a':
                ans.append(2)
                break
            elif i+2 < n and s[i+2] == 'a':
                ans.append(3)
            elif i+3 < n and s[i+1] != s[i+2] and s[i+3] == 'a':
                ans.append(4)
            elif i+6 < n and s[i+1] == s[i+2] and s[i+3] == 'a' and s[i+6] == 'a' and s[i+4] == s[i+5]:
                if s[i+1] == s[i+4]:
                    continue
                ans.append(7)
    if ans:
        print(min(ans))
    else:
        print(-1)