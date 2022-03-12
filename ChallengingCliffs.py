for t in range(int(input())):
    n = int(input())
    h = list(map(int,input().split()))
    h.sort()
    dif = h[1]-h[0]
    ind = 1
    for i in range(1,n-1):
        if h[i+1]-h[i] < dif:
            dif = h[i+1]-h[i]
            ind = i+1
    ans = h[ind-1:ind]+h[ind+1:]+h[:ind-1]+h[ind:ind+1]
    print(*ans)
