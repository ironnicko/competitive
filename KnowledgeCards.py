for _ in range(int(input())):
    n,m,k = map(int, input().split())
    arr = list(map(int, input().split()))
    idx = [i for i in range(k, 0, -1)]
    ans = "YA"
    
    if n*m-3 < k:
        mx = 0
        for i in range(k):
            if arr[i] > idx[i]:
                mx = max(mx, arr[i] - idx[i])
        if n*m-4 < mx:
            ans = "TIDAK"
    print(ans)
        