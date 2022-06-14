from sys import stdin, stdout
from collections import Counter

print = stdout.write
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    count = Counter([int(i) for i in input().rstrip().split()])
    single, above = 0, 0
    for i in count.values():
        if i == 1: single += 1
        else: above += 1
    print(str(above + (single + 1)//2 )+"\n")
        