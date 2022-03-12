n, k, x = map(int, input().split())
a = [int(i) for i in input().split()]
a = sorted(a)

diff = []

for i in range(1, n):
    d = a[i] - a[i-1]
    if d > x:
        diff.append( (d-1)//x )

diff = sorted(diff)
n  = len(diff)

for i in diff:
    if k >= i:
        k -= i
        n -= 1

print(n + 1)