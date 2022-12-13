from heapq import heapify, heappop, heappush
from collections import deque


class Node:
    def __init__(self, val):
        self.first = val[0]
        self.second = val[1]

    def __lt__(self, obj2):
        return (self.first + self.second) < (obj2.first + obj2.second)

    def __sub__(self, obj2):
        return abs((self.first - obj2.first) - (self.second-obj2.second))


for _ in range(int(input())):
    n = int(input())
    h = []

    for _ in range(n):
        heappush(h, Node(tuple(map(int, input().split()))))

    arr = deque([Node((0, 0))]) + deque()
    for _ in range(n):
        node = heappop(h)
        arr.appendleft(node)

    ans = (arr[(n+1)//2] - arr[(n+2)//2]) + 1
    print(ans)
