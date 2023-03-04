from math import gcd

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    pref = [0]
    for i in arr:
        pref.append(pref[-1] + i)
    del pref[0]
    to = sum(arr)
    idx = 0
    ans = 0

    for i in pref:
        if i < to:
            ans = max(ans, gcd(i, to - i))
    print(ans)
