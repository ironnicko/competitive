for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    cost = [0] * n
    for i in range(1, n-1):
        cost[i] = max(0, a[i+1]-a[i]+1, a[i-1]-a[i]+1)
    if n & 1:
        print(sum(cost[1::2])) # if the number of buildings is odd, just take the sum of costs starting from the 1st building through [first building meaning the peak]
    else:
        mn = C  = sum(cost[2::2])
        # dra
        for i in range(1, n-1, 2):
            C -= cost[i+1]
            C += cost[i]
            mn = min(C, mn)
        print(mn)
