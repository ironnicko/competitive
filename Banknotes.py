from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n, k = map(int, input().rstrip().split())
    a = [int(i) for i in input().rstrip().split()]
    res = 0
    k += 1
    for i in range(n):
        mul = k
        if i+1 < n:
            mul = min(mul, (10**(a[i+1]-a[i]))-1)
        res += (10**(a[i]))*mul
        k -= mul
    print(f"{res}\n")