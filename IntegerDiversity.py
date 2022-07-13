from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = Counter([abs(int(i)) for i in input().split()])
    a[0] = 0
    ans = 0
    for i in a:
        ans += min(2, a[i])
    print(ans - int(a[0] != 0))