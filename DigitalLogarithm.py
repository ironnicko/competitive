from heapq import heapify, heappop, heappush
for _ in range(int(input())):
    N = int(input())
    A = [-x for x in [*map(int, input().split())]]
    B = [-x for x in [*map(int, input().split())]]
    heapify(A)
    heapify(B)
    ans = 0
    while len(A) and len(B):
        x, y = heappop(A), heappop(B)
        if x != y:
            ans += 1
            if x < y:
                heappush(B, y)
                heappush(A, -len(str(-x)))
            else:
                heappush(A, x)
                heappush(B, -len(str(-y)))
    print(ans)
