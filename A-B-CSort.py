from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().rstrip().split()]
    for i in range(n-1, 0, -2):
        if a[i-1] > a[i]:
            a[i], a[i-1] = a[i-1], a[i]
    print("YES" if sorted(a) == a else "NO")