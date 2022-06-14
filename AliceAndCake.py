from collections import Counter
from sys import stdin
input = stdin.readline

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    a = [int(i) for i in input().rstrip()]
    count = Counter(a)
    a = [sum(a)]
    visited = set()


