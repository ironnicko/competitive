for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[0 for _ in range(n+1)] for __ in range(n+1)]

    def LIS(i, picked):
        if i == n:
            return 0
        if dp[i][picked+1]:
            return dp[i][picked+1]
        notTake = LIS(i+1, picked)
        take = 0
        if picked == -1 or (arr[i] > arr[picked] and arr[i] % arr[picked] == 0):
            take = 1 + LIS(i+1, i)
        dp[i][picked+1] = max(take, notTake)
        return dp[i][picked+1]
        
    # print(LIS(0, -1))
    for i in range(n, 0, -1):
        for j in range(i*2, n, i):
            notTake = dp[i][j+1]
            take = 1 + dp[i][i+1]
            dp[i-1][j+1] = max(notTake, take)
    print(max(max(dp)))