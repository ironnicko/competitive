from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print = stdout.write

input()
z=[0]*100001
for i in map(int,input().split()):
    z[i]+=i
a=0
b=0
for i in z:
    a,b=max(a,i+b),a
print(f"{a}\n")
