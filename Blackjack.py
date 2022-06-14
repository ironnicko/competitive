from sys import stdin, stdout

print = stdout.write
input = stdin.readline

a=int(input())

score = 0
if a > 10 and a < 22:
    a -= 10
    score += 4
    if a == 10:
        score += 11
print(f"{score}\n")