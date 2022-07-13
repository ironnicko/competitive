from collections import Counter
from sys import stdin
input = stdin.readline

def recurse(s):
    if c.get(s, 0):
        c[s]-=1
        return 1
    return s>1 and recurse( s//2 ) and recurse( s//2 + (s&1) )

for _ in range(int(input())):
    input()
    a=list(map(int,input().split()))
    c=Counter(a)
    print(("NO", "YES")[recurse(sum(a))])