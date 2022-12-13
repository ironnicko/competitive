for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    diff = set()
    if n < 3:
        print(0)
        continue
    mx = -1
    for i in range(n-1):
        d = arr[i+1] - arr[i]
        mx = max(arr[i], mx)
        diff.add(d)
    if len(diff) > 2:
        print(-1)
        continue
    if len(diff) == 1:
        print(0)
        continue
    a, b = diff.pop(), diff.pop()

    if (a <= 0 and b <= 0):
        print(-1)
        continue
    if a >= 0 and b >= 0:
        print(-1)
        continue
    a, b = max(a, b), min(a, b)
    if (mx > abs(a)+abs(b)):
        print(-1)
    else:
        print(a-b, min(a,b))
