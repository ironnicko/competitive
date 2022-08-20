for _ in range(int(input())):
    n = int(input())
    a = [0]*n
    d = [[0] for i in range(n)]
    for i, j in sorted(zip(map(int, input().split()), map(int, input().split())), key=lambda x:x[1]):
        d[i-1].append(d[i-1][-1] + j)

    for i in range(n):
        for j in range(1, len(d[i])):
            a[j-1] += d[i][-1] - d[i][(len(d[i])-1)%j]
    print(' '.join(map(str, a)))