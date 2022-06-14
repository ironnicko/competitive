from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    s = input().rstrip()
    ans = 0
    for i in range(0, n-1, 2):
        if s[i] != s[i+1]:
            ans += 1
    print(f"{ans}\n")