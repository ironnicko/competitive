for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted([int(i) for i in input().split()], reverse=1)
    sum = 0
    for  i in range(1, n-1):
        sum += a[i] + 1
    sum += (a[0] * 2) + 2
    if sum > m: print("NO")
    else: print("YES")