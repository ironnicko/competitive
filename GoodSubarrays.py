for _ in range(int(input())):
    n = int(input())
    arr = [-1] + list(map(int, input().split()))
    dp = [0 for _ in range(n+1)]

    dp[1] = 1
    ans = 0
    score = 1
    for i in range(1, n+1):
        ans = 0
        if arr[i] < i:
            score = max(score, i - arr[i] + 1)
            ans = i - score
        else:
            ans = i - score
        dp[i] = dp[i-1] + 1 + ans
    print(dp[-1])