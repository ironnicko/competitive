MOD = 1000000007


n, k = map(int, input().split())
dp = [[0 for _ in range(n+1)] for __ in range(k+1)]

for i in range(1, n+1):
    dp[1][i] = 1
for i in range(1, k):
    for j in range(1, n+1):
        c = 1
        while j * c <= n:
            dp[i+1][j*c] += dp[i][j]
            c += 1
print(sum(dp[k]) % MOD)
