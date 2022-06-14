from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().rstrip().split()]
    count = [0, 0]
    for i in a:
        count[i&1] += 1
    print(f"{min(count)}\n")