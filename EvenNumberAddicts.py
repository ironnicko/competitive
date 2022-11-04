for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    odd = 0
    for i in arr:
        odd += int(i & 1)
    even = n - odd

    if odd % 4 == 2:
        cond = 0
    elif odd % 4 == 3:
        cond = 1
    elif odd % 4 == 0:
        cond = 1
    elif even & 1:
        cond = 1
    else:
        cond = 0
    print(("Bob", "Alice")[cond])