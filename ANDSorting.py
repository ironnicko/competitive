from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().rstrip().split()]
    m = -1
    for i in range(n):
        if i != a[i]:
            m &= (-1 if i == 0 else a[i])
    print(str(m)+"\n")
