from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for j in range(int(input())):
    n=int(input());a=list(map(int,input().split()))
    cnt=0;x=0
    for i in range(n):
        x=max(x,a[i])
        if x==i+1:cnt+=1
    print(cnt)


# def find(node, par):
#     res = node-1
#     while res != par[res]:
#         par[res] = par[par[res]]
#         res = par[res]
#     return res
# def union(node1, node2, rank, par):
#     p1, p2 = find(node1, par), find(node2, par)
#     if p1 == p2:
#         return 0
#     if rank[p2] > rank[p1]:
#         par[p1] = p2
#         rank[p2] += rank[p1]
#     else:
#         par[p2] = p1
#         rank[p1] += rank[p2]
#     return 1

# for _ in range(int(input())):
#     n = int(input())
#     a = [int(i) for i in input().rstrip().split()]
#     par = [i for i in range(n)]
#     rank = [1] * n
#     res = n
#     for i in range(n):
#         for j in range(i+1, n):
#             if a[i] > a[j]:
#                 res -= union(a[i], a[j], rank, par)
#     print(str(res)+"\n")
