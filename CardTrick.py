from sys import stdin,stdout
from collections import deque, Counter
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    a = deque([int(i) for i in input().rstrip().split()])
    c = int(input())
    ci = [int(i) for i in input().rstrip().split()]
    count = Counter(ci)
    score = 0
    visited = deque()
    for i in ci:
        score += i
    ans = a[score%n]
    print(str(ans)+"\n")
    