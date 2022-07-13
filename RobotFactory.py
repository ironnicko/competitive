# import os,sys
# from io import BytesIO,IOBase
# BUFSIZ=8192
# class FastIO(IOBase):
#     newlines=0
#     def __init__(self,file):
#         self._fd=file.fileno()
#         self.buffer=BytesIO()
#         self.writable="n"in file.mode or "r" not in file.mode
#         self.write=self.buffer.write if self.writable else None
#     def read(self):
#         while True:
#             b=os.read(self._fd,max(os.fstat(self._fd).st_size,BUFSIZ))
#             if not b:
#                 break
#             ptr=self.buffer.tell()
#             self.buffer.seek(0,2),self.buffer.write(b),self.buffer.seek(ptr)
#         self.newlines=0
#         return self.buffer.read()
#     def readline(self):
#         while self.newlines==0:
#             b=os.read(self._fd,max(os.fstat(self._fd).st_size, BUFSIZ))
#             self.newlines=b.count(b"\n")+(not b)
#             ptr=self.buffer.tell()
#             self.buffer.seek(0, 2),self.buffer.write(b),self.buffer.seek(ptr)
#         self.newlines-=1
#         return self.buffer.readline()
#     def flush(self):
#         if self.writable:
#             os.write(self._fd,self.buffer.getvalue())
#             self.buffer.truncate(0),self.buffer.seek(0)
# class IOWrapper(IOBase):
#     def __init__(self, file):
#         self.buffer=FastIO(file)
#         self.flush=self.buffer.flush
#         self.writable=self.buffer.writable
#         self.write=lambda s:self.buffer.write(s.encode("ascii"))
#         self.read=lambda:self.buffer.read().decode("ascii")
#         self.readline=lambda:self.buffer.readline().decode("ascii")
# if sys.version_info[0]<3:
#     sys.stdin,sys.stdout=FastIO(sys.stdin),FastIO(sys.stdout)
# else:
#     sys.stdin,sys.stdout=IOWrapper(sys.stdin),IOWrapper(sys.stdout)
# input=lambda:sys.stdin.readline().rstrip("\r\n")


def dfs(idx):
	dp[idx] = 1
	ans = 1
	v = [(idx)]
	while v:
		idx = v.pop()
 
		for d1 in graphs[idx]:
			if dp[d1]==-1:
				dp[d1]=1
				v.append((d1))
				ans += 1
	return ans


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
graphs = [[] for _ in range(n*m)]

# adjacency list or the rooms 
for i in range(n):
    for j in range(m):

		# right
        if j+1<m and arr[i][j]&(1<<2)==0 and arr[i][j+1]&1==0:
            graphs[i*m+j].append(i*m+j+1)
            graphs[i*m+j+1].append(i*m+j)
		# down
        if i+1<n and arr[i][j]&(1<<1)==0 and arr[i+1][j]&(1<<3)==0:
            graphs[i*m+j].append((i+1)*m+j)
            graphs[(i+1)*m+j].append(i*m+j)

dp = [-1]*(m*n)
final =[]

for i in range(n):
    for j in range(m):
        if dp[i*m + j] == -1:
            final.append(dfs(i*m + j))
final = sorted(final, reverse=1)
print(" ".join(map(str, final)) + " ")
