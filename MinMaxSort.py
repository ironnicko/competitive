
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    idx = [-1 for _ in range(n+1)]
    final = 0
    for x, i in enumerate(arr):
        idx[i] = x
    for i in range(1, n):
        if idx[i] > idx[i+1]:
            final = max(final, min(i, n-i))
    print(final)
