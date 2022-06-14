for _ in range(int(input())):
    n = int(input())
    string = input()
    dots = string.count('*')
    b = 0
    ans = 0
    for i in string:
        if i == '*':
            b+=1
        else:
            ans += min(b, dots - b)
    print(ans)