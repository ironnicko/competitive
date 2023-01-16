
for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    arr.sort()
    for i in range(m):
        f = 0
        for j in range(n):
            if brr[i] > arr[j]:
                arr[j] = brr[i]
                f = 1
                break
        if not f:
            arr[0] = brr[i]
        else:
            f = 0

    arr.sort()
    print(sum(arr))
