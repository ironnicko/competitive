from array import array
import itertools
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

def ans2():
    from collections import Counter
    from itertools import combinations

    int(input())
    arr = Counter([i%10 for i in map(int, input().split())])
    fun = []
    for i, x in arr.items():
        fun += [i] * min(3, x)
    def ans():
        for comb in combinations(fun, 3):
            if sum(comb) % 10 == 3:
                print("YES")
                return
        print("NO")
    ans()

# More efficient with lookup tables
def ans1():
    int(input())
    a = []
    look_up = {}
    for i in input().split():
        look_up[int(i[-1])] = look_up.get(int(i[-1]), 0)+1
        if look_up[int(i[-1])] == 4:
            look_up[int(i[-1])] -= 1
        else:
            a.append(int(i[-1]))
    def ans():
        n = len(a)
        for i in range(n):
            for j in range(i+1, n):
                look_up[a[i]] -= 1
                look_up[a[j]] -= 1
                if a[i] + a[j] > 13:
                    exp = 23 - a[i] - a[j]
                elif a[i] + a[j] > 3:
                    exp = 13 - a[i] - a[j]
                else:
                    exp = 3 - a[i] - a[j]
                if look_up.get(exp, -1) > 0 :
                    print("YES")
                    return
                look_up[a[i]] += 1
                look_up[a[j]] += 1
        print("NO")
    ans()

for _ in range(int(input())):
    ans1()


