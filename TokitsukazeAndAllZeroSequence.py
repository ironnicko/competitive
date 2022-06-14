from collections import Counter
from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    a =[int(i) for i in input().rstrip().split()]
    numbers = 0
    f1 = 0
    for i in a:
        if i != 0:
            numbers += 1
        else:
            f1 = 1
    f2 = 0
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            f2 = 1
            break
    if f1 or f2:
        print(str(numbers)+"\n")
    else:
        print(str(numbers+1)+"\n")