from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print =lambda x : stdout.write(str(x))

for _ in range(int(input())):
    n = int(input())
    a, b = list(map(int, input().split())), list(range(1, n+1))
    if n == 1:
        print(-1)
        print("\n")
        continue
    i=0
    while i < n-1:
        if a[i] == b[i]:
            temp = b[i]
            b[i] = b[i+1]
            b[i+1] = temp
            i+=1
        i+=1
    if b[n-1] == a[n-1]:
        temp = b[n-2]
        b[n-2] = b[n-1]
        b[n-1] = temp
    for i in range(n):
        print(b[i])
        print(" ")
    print("\n")