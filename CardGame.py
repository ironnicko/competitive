from math import comb
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

arr = []
for _ in range(int(input())):
    n = int(input())
    arr.append(n)

MOD = 998244355

def solve():
    DP = [0] * (35)
    dp = [0] * (35)
    for k in range(1, 31):
        P = 1
        n = k * 2
        for i in range(n//2):
            P *= (n-i)
            P //= i+1
        DP[k] = 1
        for i in range(n//2):
            DP[k] = DP[k] * (n - 1 - i)
            DP[k] = DP[k] // (i+1)
        DP[k] = (DP[k] + dp[k-1]) % (MOD-2)
        dp[k] = (P - DP[k]-1) % (MOD-2) # current combination - the wins of A - 1 gives us the answer for the given N

    for idx in arr:
        print(DP[idx//2], dp[idx//2], 1)
solve()