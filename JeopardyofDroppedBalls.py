def find(x, y):
    if par[x][y] != (x,y):
        par[x][y] = find(par[x][y][0], par[x][y][1])
    return par[x][y]
def union(x, y, i, j):
    parx, pary = find(x,y), find(i,j)
    if parx != pary:
        par[x][y] = pary

def helper(x,y):
    while x < n:
        if arr[x][y] == 1:
            arr[x][y] = 2
            union(x, y, x+1, y)
            y+=1
        elif arr[x][y]==3:
            arr[x][y] = 2
            union(x, y, x+1, y)
            y-=1
        else:
            x, y = find(x,y)
    print(y+1, end=" ")

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

K = list(map(int, input().split()))

par = [[(i, j) for j in range(m)] for i in range(n+1)]

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if arr[i][j] == 2:
            union(i, j, i+1, j)

for i in range(k):
    helper(0, K[i]-1)