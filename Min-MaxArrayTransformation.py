from bisect import bisect_left

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    ns = int(n)
    ans1 = [0] * ns
    ans = [0] * ns
    for i in range(n-1, -1, -1):
        iter = bisect_left(b, a[i])
        ans1[i] = b[iter] - a[i]
        ans[i] = b[ns-1] - a[i]
        if iter == i:
            ns = i
    print(*ans1)
    print(*ans)