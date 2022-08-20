for _ in range(int(input())):
    n, q = map(int, input().split())
    maxima = [0]*n
    so = 0
    arr =list(map(int, input().split()))
    for i in range(1, n):
        if arr[so] > arr[i]:
            maxima[so]+=1
        else:
            maxima[i] += 1
            so = i
    maxima[arr.index(n)] = float('inf')
    while q:
        number, r = map(int, input().split())
        r -= max(0, number-2)
        r = max(0, r)
        print(min(r, maxima[number-1]))
        q-=1