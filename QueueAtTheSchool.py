from sys import stdin,stdout
input = stdin.readline
print = stdout.write

n, x = map(int, input().rstrip().split())
s = list(input().rstrip())
for _ in range(x):
    a = []
    for j in range(n-1):
        if s[j] == 'B' and s[j+1] == 'G': a.append(j)
    for x in a:
        s[x], s[x+1] = 'G', 'B'
 
print("".join(s))
