from sys import stdin,stdout
from collections import defaultdict
input = stdin.readline
print = stdout.write
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

inf = float('inf')
ans = 0 
n, m = map(int, input().split())
row = BIT(n + 2)
col = BIT(n + 2)
rcnt = [0] * (n + 1)
ccnt = [0] * (n + 1)
cnt = defaultdict(int)

for i in range(m):
    ops = list(map(int, input().split()))
    if ops[0] == 1:
        x, y = ops[1], ops[2]
        if cnt[(x, y)] == 0:
            if rcnt[x] == 0:
                row.add(x, 1)
            rcnt[x] += 1 

            if ccnt[y] == 0:
                col.add(y, 1)
            ccnt[y] += 1 
        cnt[(x, y)] += 1 
    elif ops[0] == 2:
        x, y = ops[1], ops[2]
        if cnt[(x, y)] == 1:
            if rcnt[x] == 1:
                row.add(x, -1)
            rcnt[x] -= 1 

            if ccnt[y] == 1:
                col.add(y, -1)
            ccnt[y] -= 1 
        cnt[(x, y)] -= 1 
    else:
        x1, y1, x2, y2 = ops[1:]
        flag = False 
        
        rc = row.get_sum(x2) - row.get_sum(x1 - 1)
        if rc == x2 - x1 + 1:
            flag = True 
        
        cc = col.get_sum(y2) - col.get_sum(y1 - 1)
        if cc == y2 - y1 + 1:
            flag = True 
        print(str("YES" if flag else "NO")+"\n")
