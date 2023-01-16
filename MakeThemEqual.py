B = 1001
dp = [B] * B
dp[0] = dp[1] = 0
for i in range(1, B):
    for j in range(1, i + 1):
        m = i + i // j
        if m < B:
            dp[m] = min(dp[m], dp[i] + 1)
 

for _ in range(int(input())):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    for i in range(n):
        b[i] = dp[b[i]]
    k = min(k, int(2e4))
    ans = [0] * (k+1)
 
    for i in range(n):
        for j in range(k, b[i]-1, -1):
            ans[j] = max(ans[j], ans[j-b[i]] + c[i])
 
    print(ans[k])
    