for _ in range(int(input())):
    n, k = map(int, input().split())
    F = False
    arr=  []
    for i in range(1, n+1, 2):
        if k & 1 == 0:
            a,b = ((i+1, i), (i, i+1))[F]
            F = not F
        else:
            a,b = (i, i+1)
        if (((a + k)*b) % 4) != 0:
            arr = []
            break
        arr.append((a, b))
    if len(arr):
        print("YES")
        for i in arr:
            print(*i)
    else:
        print("NO")