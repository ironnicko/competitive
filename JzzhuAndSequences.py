from sys import stdin,stdout

input = lambda : stdin.readline().rstrip()
print = stdout.write

x, y = map(int, input().split())
n = int(input())
print(str((x,y,y-x,-x,-y,x-y,x,y,y-x)[(n-1)%6]%1000000007))