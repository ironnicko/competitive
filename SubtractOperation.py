from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print =lambda x : stdout.write(str(x))

for _ in range(int(input())):
    n, k = map(int, input().split())
    f = 1
    res = {int(i) : 1 for i in input().split()}
    for i in res.keys():
        if res.get(i-k, 0):
            print("YES\n")
            f = 0
            break
    if f:
        print("NO\n")