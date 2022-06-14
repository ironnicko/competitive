from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print =lambda x : stdout.write(str(x)+"\n")

for _ in range(int(input())):
    n, q = map(int, input().split())
    a = [int(i) for i in input().split()]
    d1 = [0 for _ in range(n+1)]
    d2 = [0 for _ in range(n+1)]
    d1[0] = float("-inf")
    d2[0] = 0
    for i in range(n):
        d1[i+1] = max(d1[i], d2[i]+a[i])
        d2[i+1] = max(d2[i], d1[i] - a[i])

    print(max(d1[-1], d2[-1]))