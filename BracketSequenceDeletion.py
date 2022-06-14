for _ in range(int(input())):
    n = int(input())
    s = input()[:n]
    ans, remove = 0, 0
    s_copy = ""
    for i in range(n):
        s_copy += s[i]
        if s_copy == "()" or s_copy == "((" or s_copy == "))":
            ans += 1
            remove += 2
            s_copy = ""
        elif len(s_copy)>1:
            if s[i] == ")":
                ans += 1
                remove += len(s_copy)
                s_copy = ""
    print(ans, n-remove)