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


for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [0 for _ in range(n)]
    mx = 0
    for i in map(int, input().split()):
        a[i-1]+=1
        mx = max(mx, a[i-1])
    l = 0
    r = mx
    mid = (l+r)//2

    def check(t):
        tot  =0
        for i in range(n):
            if t > a[i]:
                tot -=( t - a[i])//2

            else:
                tot += a[i] - t
        return tot <= 0

    while r-l > 1:
        if check(mid):

            r = mid
        else:
            l = mid
        mid =  (l+r)//2
    print(r)