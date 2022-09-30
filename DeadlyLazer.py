
for _ in range(int(input())):
    m,n,a,b,d=map(int,input().split())

    if (d< b-1 and d < m-a) or (d < a-1 and d < n-b):
        print(m+n-2)
    else:
        print(-1)