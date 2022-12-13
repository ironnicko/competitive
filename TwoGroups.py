for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    second = 0
    third = 0
    for i in arr:
        if i < 0:
            second += i
        else:
            third += i
    print(max(abs(third + second), sum(arr)))
