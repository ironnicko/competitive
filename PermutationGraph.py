import heapq

class HeapEntry:
    def __init__(self, node, priority):
        self.node = node
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority


class Graph:
    def __init__(self, graph):
        self.nodes = {}

    def add_node(self, key, neighbours):
        self.nodes[key] = neighbours

    def traceback_path(self, target, parents):
        path = []
        while target:
            path.append(target)
            target = parents[target]
        return list(reversed(path))

    def shortest_path(self, start, finish):
        OPEN = [HeapEntry(start, 0.0)]
        CLOSED = set()
        parents = {start: None}
        distance = {start: 0.0}

        while OPEN:
            current = heapq.heappop(OPEN).node

            if current is finish:
                return self.traceback_path(finish, parents)

            if current in CLOSED:
                continue

            CLOSED.add(current)

            for child in self.nodes[current]:
                if child in CLOSED:
                    continue
                tentative_cost = distance[current] + self.nodes[current][child]

                if child not in distance.keys() or distance[child] > tentative_cost:
                    distance[child] = tentative_cost
                    parents[child] = current
                    heap_entry = HeapEntry(child, tentative_cost)
                    heapq.heappush(OPEN, heap_entry)



for _ in range(int(input())):
    n = int(input())

    a = [int(i) for i in input().split()]
    dp = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        mini = a[i]
        maxi = a[i]
        for j in range(i, n):
            mini = min(mini, a[j])
            maxi = max(maxi, a[j])
            dp[i][j] = (mini, maxi)
    graph = {}
    g = Graph(graph)
    for i in range(n):
        for j in range(i+1, n):
            if ( (dp[i][j][0] == a[j] and dp[i][j][1] == a[i])
            or (dp[i][j][0] == a[i] and dp[i][j][1] ==a[j]) ):
                graph[i] = graph.get(i, [])
                graph[i].append(j)
                graph[j] = graph.get(j, [])
                graph[j].append(i)
                g.add_node(i, {j : a[j]})
                g.add_node(j, {i : a[i]})
    print(len(g.shortest_path(0, n-1)))
