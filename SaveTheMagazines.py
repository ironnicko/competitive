for _ in range(int(input())):
    n = int(input())
    s = input()
    m = list(map(int, input().split()))
    dp = [[0, 0] for i in range(n)]

    # here the states are the two pairs
    # first is the take DP part
    # second is the notTake DP part
    # the states are the take and notTake basically

    if s[0] == '1':
        dp[0][0] = 0
        dp[0][1] = m[0]
    for i in range(1, n):
        if s[i] == '1':
            # here we take the max from the take and not take of the previous state and add the ith books to it because this is the take state
            dp[i][1] = max(dp[i-1])+m[i]
            # here we update the notTake part for the current state by adding the (i-1)th book since we will be switching the lids
            dp[i][0] = dp[i-1][0]+m[i-1]
        else:
            # here we update the states to whatever was the greatest in the previous state since no changes will be done if we don't have a lid to operate with
            dp[i][1] = max(dp[i-1])
            dp[i][0] = max(dp[i-1])
    print(max(dp[-1]))
