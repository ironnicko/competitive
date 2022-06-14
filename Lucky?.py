from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    a  = list(map(int, list(input().rstrip())))
    if sum(a[:3]) == sum(a[3:]):
        print("YES\n")
    else:
        print("NO\n")
