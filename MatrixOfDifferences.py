from collections import deque
for _ in range(int(input())):
    n = int(input())
    main = deque(range(1, (n*n) + 1))
    arr = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        if i & 1:
            for j in range(n-1, -1, -1):
                if j & 1:
                    arr[i][j] = main.popleft()
                else:
                    arr[i][j] = main.pop()
        else:
            for j in range(n):
                if j & 1:
                    arr[i][j] = main.pop()
                else:
                    arr[i][j] = main.popleft()
    for i in arr:
        print(*i)
