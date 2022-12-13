
from math import gcd

MOD = int(1e5+1)

for _ in range(int(input())):
    n = int(input()) % MOD
    arr = sorted(map(int, input().split()))
    common = 0

    for i in arr:
        common = gcd(common, i)
    print(arr[-1]//common)
