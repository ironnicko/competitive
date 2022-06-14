for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    s = input()
    b = []
    r = []
    for i in range(n):
        if(s[i] == "R"):
            r.append(l[i])
        else:
            b.append(l[i])
    b = sorted(b)
    r = sorted(r)[::-1]
    ok = True
    for i in range(len(b)):
        if(b[i]<i+1):
            ok = False
    for i in range(len(r)):
        if(r[i]>n-i):
            ok = False
    print("YES") if ok else print("NO")