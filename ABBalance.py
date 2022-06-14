from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    s = list(input().rstrip())
    s[0] = (s[-1] if s[0]!=s[-1] else s[0])
    print(f"{''.join(s)}\n")