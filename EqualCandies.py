from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().rstrip().split()]
    sum = 0
    num = min(a)
    for i in a:
        sum +=  i-num
    print(str(sum)+"\n")