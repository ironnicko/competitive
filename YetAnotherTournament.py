from bisect import bisect_left, bisect_right

for _ in range(int(input())):

    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    cpy = list(arr)
    arr.sort()
    for i in range(1, n):
        arr[i] += arr[i-1]
    W = bisect_right(arr, m)
    ans = n + 1 - W
    if W > 0 and m >= (arr[W-2], 0)[W == 1] + cpy[W - int(W == n)]:
        ans -= 1
    print(max(1, ans))
