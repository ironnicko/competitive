from re import S


for _ in range(int(input())):
    s = list(input())
    c = input()
    flag = False
    for i in range(len(s)):
        if s[i] == c and (i-1)%2:
            flag = True
            break
    print("YES") if flag else print("NO")