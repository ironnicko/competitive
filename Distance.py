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

# for _ in range(int(input())):
#     x, y = map(int, input().split())
#     print((f"{x//2} {y//2 + x%2}", "-1 -1")[(x+y)&1])


for _ in range(int(input())):
    n, m  = map(int, input().split())
    s = input()
    final = 0
    while m:
        i1, i2= map(int, input().split())
        main = {}
        parity= [0, 0]
        for i in range(i1-1, i2):
            main[s[i]] = main.get(s[i], 0)+1
        for i in main:
            parity[main[i]&1]+=1
        if parity[1] == 1 and (i2-i1+1)&1:
            final += 1
        elif parity[1] == 0 and (i2-i1+1)&1 == 0:
            final += 1
            
        m-=1
    print(f"Case #{_+1}: {final}")