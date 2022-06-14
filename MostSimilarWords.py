from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n, m = map(int, input().rstrip().split())
    a = [input().rstrip() for _ in range(n)]
    ans = float('inf')
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(m):
                sum += abs(ord(a[i][k]) - ord(a[j][k])) #- 2*(ord('a'))
            ans = min(sum, ans)
            sum = 0
    print(str(ans) + "\n")