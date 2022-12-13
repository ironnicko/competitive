for _ in range(int(input())):
    m, s = map(int, input().split())

    arr = set(map(int, input().split()))
    count = 1
    while s > 0:
        s -= count * int(count not in arr)
        arr.add(count)
        count += 1
    print(("NO", "YES")[s == 0 and max(arr) == len(arr)])
