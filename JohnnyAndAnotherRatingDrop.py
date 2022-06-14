from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    ans = 0
    for bit in range(64, -1 , -1):
        if n & 1<<bit:
            ans += (1<<(bit+1)) - 1
    print(str(ans) + '\n')
