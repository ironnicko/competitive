from math import ceil, floor
for _ in range(int(input())):
    n, k = map(int, input().split())
    n %= int(1e9 + 7)
    p = list(map(int, input().split()))

    curr = 1

    for i in p:
        curr += int(i == curr)

    ans = n - curr + 1

    if ans % k == 0:
        ans //= k
    else:
        ans //= k
        ans += 1
    print(ans)
