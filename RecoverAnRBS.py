for _ in range(int(input())):
    s = list(input())
    o,c=  0, 0
    for i in s:
        if i == '(': c += 1
        elif i == ')': c-=1
        else :
            o += 1
        if 1-c == o:
            o = 0
            c = 1
    print(("NO", "YES")[o==c])