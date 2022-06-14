from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n, m = map(int, input().rstrip().split())
    a = [[i for i in input().rstrip()] for __ in range(n)]
    f = 1
    ans = "YES\n"
    for i in range(n):
        if not f: break
        for j in range(m):
            if not f: break
            if a[i][j] == 'R':
                for i2 in range(i+1, n):
                    for j2 in range(0, j):
                        if a[i2][j2] == "R":
                            f = 0
                            ans = "NO\n"
                            break
    print(ans)