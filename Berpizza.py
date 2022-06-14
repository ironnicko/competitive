from sys import stdin,stdout
from heapq import heapify, heappush, heappop
from collections import deque
input = stdin.readline
print = stdout.write

heap = []
heapify(heap)
hashmap = {}
vis = [0 for _ in range(1000000)]
idx = 1
mini = 1

for _ in range(int(input())):
    q= input().rstrip().split()
    if q[0] == "1":
        m = int(q[1])
        heappush(heap, (-m, idx))
        idx += 1
    elif q[0] == "2":
        while vis[mini]:
            mini += 1
        print(f"{mini} ")
        vis[mini] = 1
        mini += 1

    else:
        while heap and vis[heap[0][1]]:
            heappop(heap)
        _, i = heappop(heap)
        print(f"{i} ")
        vis[i] =1