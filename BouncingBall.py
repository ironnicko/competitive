for _ in range(int(input())):
    n,p,k=map(int,input().strip().split())
    s=input()
    x,y=map(int,input().strip().split())
    l=[0 for _ in range(n)]
    for i in range(n-1,-1,-1):
        if s[i]=="0":
            l[i]+=x
        if i<n-k:
            l[i]+=l[i+k]
    for i in range(0,n-p+1):
        l[i+p-1]+=i*y
    print(min(l[p-1:]))