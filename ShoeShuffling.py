from collections import deque
from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().rstrip().split()]
    count = {}
    for i, x in enumerate(a):
        count[x] = count.get(x, deque())
        count[x].append(i)
    f=1
    for i in count:
        if len(count[i]) < 2:
            print("-1\n")
            f =0 
            break
    if f:
        for i in sorted(count):
            count[i].rotate()
            for j in count[i]:
                print(f"{j+1} ")
        print("\n")