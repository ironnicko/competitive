from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().rstrip().split()]
    total = sum(a)
    f=1
    div = n-1
    for i in a:
        if float(i) == (total-i)/div:
            print(f"YES\n")
            break
    else:
        print("NO\n")