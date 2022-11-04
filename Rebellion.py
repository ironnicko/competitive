for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    idx = 0

    end = n-1

    count = 0
    while idx != end:
        while arr[end] == 1 and end > 0:
            end -= 1
        while arr[idx] == 0 and idx < n-1:
            idx += 1
        if idx >= end: break

        count += 1
        end -= 1
        idx += 1
    print(count)