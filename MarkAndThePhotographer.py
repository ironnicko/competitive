for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    a.sort()
    flag = 1
    for i in range(n):
        if (a[i+n] - a[i]) < k:
            flag = 0
            break
    print(("NO", "YES")[flag])