
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    s = sum(a)

    cur = [0,0]
    for i in range(n):
        cur[i&1] += a[i]-1
    for j in range(2):
        if 2 * cur[j] > s:
            continue
        elif 2 * cur[j] <= s:
            for i in range(n):
                a[i] = (a[i], 1)[i&1 == j]
        break
    print(*a)