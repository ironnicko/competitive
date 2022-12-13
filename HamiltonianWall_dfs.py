def dfs(i, j, SET):
    if i < 0 or j < 0 or j >= n or i > 1 or (i, j) in SET or grid[i][j] == 'W':
        return 0
    SET.add((i, j))
    dfs(i+1, j, SET)
    dfs(i, j+1, SET)
    dfs(i, j-1, SET)


for _ in range(int(input())):
    n = int(input())
    grid = [input() for _ in range(2)]
    B = set()
    f = 0
    for i in range(2):
        for j in range(n):
            if grid[i][j] == 'B':
                B.add((i, j))

    for i in range(2):
        if f:
            break
        for j in range(n):
            if f:
                break
            if grid[i][j] == 'B':
                cpy = set()
                dfs(i, j, cpy)
                if cpy == B:
                    f = 1
    print(("NO", "YES")[f])
