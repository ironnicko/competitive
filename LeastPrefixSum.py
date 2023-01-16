from heapq import heappop, heappush
for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    hp = []
    run = 0
    final = 0

    for i in range(m, n):
        run += arr[i]

        if arr[i] < 0:
            heappush(hp, arr[i])
        if run < 0:
            final += 1
            run -= 2 * heappop(hp)

    run = 0
    for i in reversed(range(1, m)):
        run -= arr[i]

        if -arr[i] < 0:
            heappush(hp, -arr[i])
        if run < 0:
            final += 1
            run -= 2 * heappop(hp)

    print(final)
