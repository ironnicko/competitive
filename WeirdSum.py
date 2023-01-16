from collections import defaultdict
n, m = map(int, input().split())
adj = [map(int, input().split()) for _ in range(n)]
ans = 0
hash = defaultdict(list)
total = 0

for i, item in enumerate(adj, start=1):
    for j, elem in enumerate(item, start=1):
        hash[elem].append((i, j))

for i in hash:

    V = hash[i]

    V.sort(key=lambda x : x[0])
    total = 0
    for i in V: 
        total += i[0]
    for i, x in enumerate(V):
        total -= x[0]
        ans += (total - ((len(V) - (i+1)) * x[0]))
    
    V.sort(key=lambda x : x[1])
    total = 0
    for i in V: 
        total += i[1]
    for i, x in enumerate(V):
        total -= x[1]
        ans += (total - ((len(V) - (i+1)) * x[1]))
    
print(ans)