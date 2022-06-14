from sys import stdin, stdout
print = stdout.write
input = stdin.readline

for i in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().rstrip().split()][::-1]
    f = 1
    c = 0
    for j in range(1,n):
        a = arr[j-1]
        b = arr[j]
        if(a==0):
            f = 0
            break
        while(b>=a):
            b = b//2
            c += 1
        arr[j] = b
    if(f):
        print(str(c)+"\n")
    else:
        print("-1\n")