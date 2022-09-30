for _ in range(int(input())):
    n = int(input())
    e = [int(i=="1") for i in input()]
    me  = [2 if i == "1" else 0 for i in input()]
    up = 0
    for i in range(n):
        if e[i] == 0 and me[i] == 2:
            up += 1
            e[i] = 2
            continue
        if i > 0:
            if e[i-1] == 1 and me[i] == 2:
                up+=1
                e[i-1] = 0
                continue
        if i < n-1:
            if e[i+1] == 1 and me[i] == 2:
                up += 1
                e[i+1] = 0
                continue

    print(up )