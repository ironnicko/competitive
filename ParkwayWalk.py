from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print =lambda x : stdout.write(str(x)+"\n")

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sum([int(i) for i in input().split()])
    print(a-m if a-m >= 0 else 0)