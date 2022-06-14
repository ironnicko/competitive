from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().rstrip().split()]
    c = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] >= a[j]:
                c += 1
    print(str(c)+"\n")