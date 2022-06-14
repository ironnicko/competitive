from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    l1, r1, l2, r2 = map(int, input().rstrip().split())
    if l1 >= l2 and l1 <= r2:
        print(f"{l1}\n")
    elif l2>=l1 and l2<=r1:
        print(f"{l2}\n")
    else:
        print(f"{l1+l2}\n")