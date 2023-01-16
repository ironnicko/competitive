for _ in range(int(input())):
    n, k = map(int, input().split())
    h = map(int, input().split())
    p = map(int, input().split())
    HP = sorted(zip(h, p), key=lambda x : x[0])
    mini = [float("inf") for i in range(n)]
    mini[-1] = HP[-1][1]
    for i in range(n - 2, -1, -1):
        mini[i] = min(mini[i + 1], HP[i][1])

    i = 0
    final = int(k)

    while i < n and final > 0:
        if HP[i][0] <= final:
            i += 1
        else:
            if k <= mini[i]:
                break
            k -= mini[i]
            final += k

    print(("NO", "YES")[i == n])
    
