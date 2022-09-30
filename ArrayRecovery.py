for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n-1):
        if arr[i+1] <= arr[i] and arr[i+1] != 0:
            arr.clear()
            arr = [-1]
            break
        arr[i+1] = arr[i] + arr[i+1]
    print(*arr)