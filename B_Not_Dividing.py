for _ in range(int(input())):
    n = int(input())

    arr = list(map(int, input().split()))
    prev = 1 << 1

    for i in range(n):

        arr[i] += int(arr[i] == 1)
    for _ in range(2):
        for i in range(n-1):
            if not (arr[i+1] % arr[i]):
                arr[i+1] += 1

    print(*arr)