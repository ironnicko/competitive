from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    s = input().rstrip()
    j = s[n//2]
    score = 0
    for i in range(n//2, n):
        if s[i] == j:
            score += 1
        else:
            break

    for i in range((n//2)-1, -1, -1):
        if s[i] == j:
            score += 1
        else: break
    print(str(score)+"\n")