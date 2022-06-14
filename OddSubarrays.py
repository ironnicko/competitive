from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().rstrip().split()]
    count = 0
    i=0
    while i < n-1:
        if a[i] > a[i+1]: 
            count += 1
            i+=2
        else:i+=1
    print(f"{count}\n")