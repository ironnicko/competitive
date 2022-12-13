from math import gcd

n = int(input())
p = 1
arr = []
for i in range(1, n):
    if gcd(i, n) == 1:
        p = (p * i) % n
        arr.append(i)
if p != 1:
    arr.pop()
print(len(arr))
print(*arr)
