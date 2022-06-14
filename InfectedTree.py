from collections import deque
from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print =lambda x : stdout.write(str(x)+"\n")

for _ in range(int(input())):
    n = int(input())
    graph = [[] for _ in range(n+1)]

    # get in the adjacency list
    for _ in range(n-1):
        u, v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    

    # find  the number of children each node has
    children = [0]*(n+1)
    children[1] = len(graph[1])
    for i in range(2,n+1):
        children[i] = len(graph[i])-1
    
    depth = [0]*(n+1)
    queue = deque([(0,1)])

    # perform a bfs and add a depth list to figure out the height of the node
    while queue:
        parent, node = queue.popleft()
        for child in graph[node]:
            if child == parent: continue
            queue.append((node, child))
            depth[child] = depth[node] + 1
    # go through the number of children and find out the number of children
    # then find the left sub tress of the node and calculate the min casualties
    min_casualties = n
    for i in range(1,n+1):
        if children[i] < 2:
            cur_casualties = 2*depth[i] + children[i] + 1
            min_casualties = min(min_casualties, cur_casualties)

    # remove the casualties from the overall and Voila! you have the answer.
    print(n-min_casualties)