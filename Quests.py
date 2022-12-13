
for _ in range(int(input())):
    n, c, d = map(int, input().split())

    arr = sorted(list(map(int, input().split())))
    def helper(k):
        const = d % (k + 1)
        const2 = (d // (k + 1))
        add = const2 * sum(arr[-1 : -(max(const, k)) - 2 : -1])
        for i in range(min(n, const), 0, -1):
            add += arr[n-i]
        return add >= c

    mx = arr[-1]
    if sum(arr[::-1][:d]) >= c:
        print("Infinity")
    elif mx * d < c:
        print("Impossible")
    else:
        lo = 1
        high = d-1
        for i in range(100):
            mid = (lo + high)//2
            if helper(mid):
                lo = mid
            else:
                high = mid
        print(high-1)