import os,sys
from io import BytesIO,IOBase
BUFSIZ=8192
class FastIO(IOBase):
    newlines=0
    def __init__(self,file):
        self._fd=file.fileno()
        self.buffer=BytesIO()
        self.writable="n"in file.mode or "r" not in file.mode
        self.write=self.buffer.write if self.writable else None
    def read(self):
        while True:
            b=os.read(self._fd,max(os.fstat(self._fd).st_size,BUFSIZ))
            if not b:
                break
            ptr=self.buffer.tell()
            self.buffer.seek(0,2),self.buffer.write(b),self.buffer.seek(ptr)
        self.newlines=0
        return self.buffer.read()
    def readline(self):
        while self.newlines==0:
            b=os.read(self._fd,max(os.fstat(self._fd).st_size, BUFSIZ))
            self.newlines=b.count(b"\n")+(not b)
            ptr=self.buffer.tell()
            self.buffer.seek(0, 2),self.buffer.write(b),self.buffer.seek(ptr)
        self.newlines-=1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd,self.buffer.getvalue())
            self.buffer.truncate(0),self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer=FastIO(file)
        self.flush=self.buffer.flush
        self.writable=self.buffer.writable
        self.write=lambda s:self.buffer.write(s.encode("ascii"))
        self.read=lambda:self.buffer.read().decode("ascii")
        self.readline=lambda:self.buffer.readline().decode("ascii")
if sys.version_info[0]<3:
    sys.stdin,sys.stdout=FastIO(sys.stdin),FastIO(sys.stdout)
else:
    sys.stdin,sys.stdout=IOWrapper(sys.stdin),IOWrapper(sys.stdout)
input=lambda:sys.stdin.readline().rstrip("\r\n")


def find(x, y):
    if par[x][y] != (x,y):
        par[x][y] = find(par[x][y][0], par[x][y][1])
    return par[x][y]
def union(x, y, i, j):
    parx, pary = find(x,y), find(i,j)
    if parx != pary:
        par[x][y] = pary

def helper(x,y):
    while x < n:
        if arr[x][y] == 1:
            arr[x][y] = 2
            union(x, y, x+1, y)
            y+=1
        elif arr[x][y]==3:
            arr[x][y] = 2
            union(x, y, x+1, y)
            y-=1
        else:
            x, y = find(x,y)
    print(y+1, end=" ")

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

K = list(map(int, input().split()))

par = [[(i, j) for j in range(m)] for i in range(n+1)]

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if arr[i][j] == 2:
            union(i, j, i+1, j)

for i in range(k):
    helper(0, K[i]-1)