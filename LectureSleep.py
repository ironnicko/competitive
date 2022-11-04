n, k = map(int, input().split())

arr = list(map(int, input().split()))

t = list(map(int, input().split()))

dp = [[0 for _ in range(k+1)] for __ in range(n+1)]

def recurr(i, score, carr):
    if i >= n:
        return score
    if dp[i][carr]:
        return dp[i][carr]
    if carr > 0:
        return recurr(i+1, score+arr[i], carr-1)
    if t[i]:
        return recurr(i+1, score+arr[i], carr)
    elif i >= n - k + 1:
        return recurr(i+1, score, -1)
    else:
        return max(recurr(i+1, score+arr[i], k-1), recurr(i+1, score, -1))
print(recurr(0, 0, -1))