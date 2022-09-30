MOD = 50000

for _ in range(int(input())):
    n,k,x,y = map(int, input().split())
    n%=MOD
    k%=MOD
    x%=MOD
    y%=MOD
    grid = []
    for i in range(501):
        grid.append([])
        for j in range(501):
            grid[i].append(".")
    for L in range(2, (n*2)+1):
        if not(abs(x + y - L) % k):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if i+j==L:grid[i][j] = 'X'
    for i in range(1, n+1):
        for j in range(1, n+1):print(grid[i][j], end="")
        print("\n", end="")