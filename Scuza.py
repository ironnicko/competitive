from bisect import bisect_right

for _ in range(int(input())):

    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    bs = []

    mx = 0
    prefix = [0]
    for i in arr:
        prefix.append(prefix[-1] + i)
    for i in arr:
        mx = max(mx, i)
        bs.append(mx)
    
    for i in map(int, input().split()):
        idx = bisect_right(bs, i)
        print(prefix[idx], end=" ")
    print()