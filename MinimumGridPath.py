from re import L


for _ in range(int(input())):
    n = int(input())

    cost = [int(i) for i in input().split()]
    step = [n,n]
    ans = float('inf')
    minC = [int(1e9) for _ in range(2)]
    sum = 0

    for i in range(n):
        sum += cost[i]

        step[i%2]-=1

        minC[i%2] = min(minC[i%2], cost[i])

        ans = min(ans, step[0]*minC[0] + step[1]*minC[1] + sum)

    print(ans)