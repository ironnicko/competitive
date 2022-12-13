from bisect import bisect_left, bisect_right

for _ in range(int(input())):
    n, l, r = map(int, input().split())

    arr = list(map(int, input().split()))
    arr.sort()

    ans = 0

    for i, x in enumerate(arr):
        left = bisect_left(arr, l-x, i+1)
        right = bisect_right(arr, r-x, i+1)
        ans += right - left
    print(ans)
