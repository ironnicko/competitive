for _ in range(int(input())):
    l, r, a = map(int, input().split())
    if a==1:
        print(r)
    elif l==r:
        print(r//a+r-(r//a)*a)
    elif r%a==a-1:
        print(r//a+a-1)
    elif r%a:
        if a*(r//a)-1>=l:
            print(r//a-1+a-1)
        else:
            print(r//a+r-(r//a)*a)
    else:
        r-=1
        print(r//a + r-(r//a) *a)
 