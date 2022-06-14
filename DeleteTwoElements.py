from sys import stdin,stdout
from collections import Counter
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().rstrip().split()))
 
    tar = sum(l) - ( (n-2) * (sum(l)/n) )
    d=Counter()
    c=0
    for i in l:
        c+=d[tar-i]
        d[i]+=1
    print(str(c)+"\n")