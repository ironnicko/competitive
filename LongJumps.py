for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        if i + arr[i] < n:
            arr[i] += arr[i + arr[i]]
        else:
            continue

    print(max(arr))