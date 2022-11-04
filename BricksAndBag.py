for _ in range(int(input())):
    n = int(input())

    arr = sorted(list(map(int, input().split())))

    ans = arr[-1] - arr[0]
    for i in range(n - 1):
        b1 = arr[i+1]
        b2 = arr[-1]
        b3 = arr[0]
        ans = max(ans, b1 + b2 - 2 * arr[i], 2 * b1 - arr[i] - b3)
    print(ans)