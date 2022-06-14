from collections import defaultdict, deque
from sys import stdin, stdout

print = stdout.write
input = stdin.readline

md = 10**9+7

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    c = list(map(int, input().rstrip().split()))
    d = defaultdict(bool)
    for i in range(n):
        d[c[i]] = True
    lonely = defaultdict(int)
    for i in range(n):
        lonely[a[i]] = i
    ans,ct = 1,0
    for i in range(n):
        if c[i]!=0 or a[i]==b[i] or d[a[i]] or d[b[i]]:
            continue
        j = lonely[b[i]]
        comb = 2
        
        while j != i:
            if c[j] != 0:
                comb = 1
            c[j] = 1
            j = lonely[b[j]]
        ans = (ans*comb)%md
    print(str(ans)+"\n")
