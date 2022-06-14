
from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    s = input().rstrip()
    c = {i for i in input().rstrip().split()}
    k = c.pop(0)
    last = -1
    last_pos = 0
    for i in range(n):
        if s[i] in c:
            if last_pos != -1:
                last = max(last, i-last_pos)
            last_pos = i
    print(str(last if last != -1 else last_pos)+"\n")

