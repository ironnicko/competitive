from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n, m = map(int, input().rstrip().split())
    a = [[int(i) for i in input().rstrip().split()] for _ in range(n)]
    diag1 = [0 for _ in range(m+n)]
    diag2 = [0 for _ in range(m+n)]
    final = 0
    for i in range(n):
        for j in range(m):
            diag1[i+j] += a[i][j]
            diag2[i-j+m] += a[i][j]
    for i in range(n):
        for j in range(m):
            final = max(final, diag1[i+j] + diag2[i - j+m] - a[i][j])
    print(str(final)+"\n")