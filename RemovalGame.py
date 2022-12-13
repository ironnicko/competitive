from collections import defaultdict
n = int(input())

arr = list(map(int, input().split()))

dp = [defaultdict(int) for _ in range(n+1)]

for l in range(n-1, -1, -1):
    for r in range(1, n):
        if l == r:
            dp[l][r] = arr[l]
        else:
            dp[l][r] = max(arr[l]-dp[l+1][r], arr[r]-dp[l][r-1])
print((sum(arr) + dp[0][n-1])//2)
