n, m = map(int, input().split())

arr = sorted(map(int, input().split()))
s=0
dp=[0]*m
for i in range(n):
    s += arr[i]
    dp += [s + dp[i]]
print(*dp[m:])
