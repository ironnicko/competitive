from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print =lambda x : stdout.write(str(x))

for _ in range(int(input())):
    n, x, y= map(int, input().split())
    a = [int(i) for i in input().rstrip().split()]
    if (sum(a) + x + y)&1:
        print("Bob\n")
    else:
        print("Alice\n") 