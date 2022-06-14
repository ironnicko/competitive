from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print = stdout.write

for _ in range(int(input())):
    n, m = map(int, input().split())
    mat = [[0 if i == "." else 1 for i in input()] for _ in range(n)]
    for i in range(n-1, 0, -1):
        for j in range(1, m-1):
            if mat[i][j-1] and mat[i][j] and mat[i][j+1] and mat[i-1][j]:
                mat[i-1][j] += min(mat[i][j-1], mat[i][j], mat[i][j+1])
    count = 0
    for i in range(n):
        count += sum(mat[i])
    print(f"{count}\n")