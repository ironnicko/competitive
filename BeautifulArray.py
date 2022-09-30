
for _ in range(int(input())):
    n, k, b,s  =map(int, input().split())

    if s < k*b or s > n*(k-1) + (k * b):
        print(-1)
    else:
        final = [0 for _ in range(n)]
        final[0] = k * b
        s -= k * b
        i = 0
        while i < n and s > 0:

            final[i] += min(k-1, s)
            s -= min(k-1, s)       
            i+=1

        print(*final[::-1])