from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().rstrip().split()]
    countMinus = 0
    f = 1
    for i in range(n):
        if a[i] < 0:
            countMinus += 1
            a[i] = -1 * a[i]
    for i in range(n):
        if countMinus > 0:
            a[i] *= -1
            countMinus -= 1

    for i in range(n-1):
        if a[i] > a[i+1]:
            print("NO\n")
            f=0
            break
    if f:
        print("YES\n")