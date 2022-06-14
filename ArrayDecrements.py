from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print =lambda x : stdout.write(str(x))

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    max_d = 0
    f=1
    for i in range(n):
        if a[i] < b[i]:
            print("NO\n")
            f = 0
            break
        max_d = max(max_d, abs(a[i] - b[i]))
    if f:
        for i in range(n):
            k  = max(a[i] - max_d, 0)
            if k == b[i]:
                continue
            print("NO\n")
            f = 0
            break
    if f:
        print("YES\n")
