MOD = int(2e6)

for _ in range(int(input())):
    n = int(input())
    n %= MOD
    array = list(map(int, input().split()))
    if (array.count(1) + array.count(-1)) & 1:
        print(-1)
    else:
        s = sum(array)
        for i in range(n):
            if i == 0:
                q = [[0, 0]]
                continue
            if abs(s) > abs(s - 2*array[i]) and q[-1][0] == i-1:
                q[-1][1] = i
                s -= 2*array[i]
            else:
                q.append([i, i])

        print(len(q))

        for x, y in q:
            print(x+1, y+1)
