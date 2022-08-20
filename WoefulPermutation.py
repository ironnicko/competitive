for _ in range(int(input())):
    n = int(input())
    arr = [i+1 for i in range(n)]
    if n & 1:
        for i in range(1, n-1, 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]
    else:
        for i in range(0, n, 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]

    print(*arr)