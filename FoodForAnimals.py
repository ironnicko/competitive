from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    a, b, c, x, y = map(int, input().rstrip().split())
    x-= a
    y -= b
    if x < 0:
        x = 0
    if y < 0:
        y = 0 
    if x+y - c <= 0:
        print("YES\n")
    else:
        print("NO\n")