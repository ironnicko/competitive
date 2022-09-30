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

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
 
    # this is where the amortized time complexity is observed

    def find(self, a):
        temp = []
        while a != self.parent[a]:
            temp.append(a)
            a = self.parent[a]
        for i in temp:
            self.parent[i] = a
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
 
 
n, m = map(int, input().split())
dsu = DSU(n)
for x in range(m):
    count, *numbers = map(int, input().split())
    if count > 1:
        temp = numbers[0]
        for y in numbers:
            dsu.union(temp, y)
ans = []
for z in range(1, n + 1):
    ans.append(dsu.size[dsu.find(z)])
print(*ans)