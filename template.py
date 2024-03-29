from collections import deque, defaultdict
from sys import stdin,stdout
input = stdin.readline
print = stdout.write

class Node:
    def __init__(self):
        self.links = [-1 for _ in range(26)]
        self.flag = 0
    def containsKey(self, char):
        return self.links[ord(char) - 97] != -1
    def put(self, char, node):
        self.links[ord(char) - 97] = node
    def get(self, char):
        return self.links[ord(char) - 97]
    def setEnd(self):
        self.flag = 1

class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        self.node = self.root
        for i in range(len(word)):
            if not(self.node.containsKey(word[i])):
                self.node.put(word[i], Node())
            self.node.get(word[i])
        self.node.setEnd()
    def search(self, word):
        self.node = self.root
        for i in range(len(word)):
            if not(self.node.containsKey(word[i])):
                return False
            self.node = self.node.get(word[i])
        return self.node.flag

    def startswith(self, prefix):
        self.node = self.root
        for i in range(len(prefix)):
            if not(self.node.containsKey(prefix[i])):
                return False
            self.node = self.node.get(prefix[i])
        return True


class Graph:
	def __init__(self, num_of_v):
		self.num_of_v = num_of_v
		self.edges = defaultdict(list)
	def add_edge(self, u, v):
		self.edges[u].append(v)
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
 
    def find(self, a):
        temp = []
        # print(a, self.parent[a])
        while a != self.parent[a]:
            temp.append(a)
            a = self.parent[a]
        for i in range(len(temp)):
            self.parent[temp[i]] = a
        return self.parent[a]
 
    def union(self, a, b):
        aa = self.find(a)
        bb = self.find(b)
        if aa == bb:
            return
        if self.size[aa] >= self.size[bb]:
            self.parent[bb] = aa
            self.size[aa] += self.size[bb]
            self.size[bb] = 1
        else:
            self.parent[aa] = bb
            self.size[bb] += self.size[aa]
            self.size[aa] = 1
# def isCycle(graph):
# 	subsets = []

# 	for u in range(graph.num_of_v):
# 		subsets.append(subset(u, 0))

# 	for u in graph.edges:
# 		u_rep = find(subsets, u)

# 		for v in graph.edges[u]:
# 			v_rep = find(subsets, v)

# 			if u_rep == v_rep:
# 				return True
# 			else:
# 				union(subsets, u_rep, v_rep)

class BIT:
    def __init__(self, n):
        self.n = n 
        self.tr = [0] * (n + 1)
    
    def lowbit(self, x):
        return x & -x 
    
    def add(self, x, c):
        i = x 
        while i <= self.n:
            self.tr[i] += c 
            i += self.lowbit(i)
        return 
    
    def get_sum(self, x):
        res = 0 
        i = x 
        while i > 0:
            res += self.tr[i]
            i -= self.lowbit(i)
        return res 
        
    def memset(self, x):
        self.tr = [x] * (self.n + 1)


def bfs(graph, node, visited=set()):
    queue = deque()
    visited.add(node)
    queue.append(node)
    while queue:
        m = queue.popleft()
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)



if __name__ == "__main__":
    graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
    }
    bfs(graph, '5')


