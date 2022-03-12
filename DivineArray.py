n = int(input())

while n:
    l = int(input())
    a = [int(x) for x in input().split()]
    q = int(input())

    ans = [a]

    found = False

    while not found:
        b = ans[-1]
        d = {}
        for i in b:
            d[i] = b.count(i)
        z = 1
        for i in d:
            if d[i] != i:
                z = 0
                break
        if z:
            break
        for i in b:
            i = d[i]
        ans.append(b)

    for i in range(q):
        xi, ki = [int(x) for x in input().split()]
        if ki >= len(ans):
            print(ans[-1][xi-1])
        else:
            print(ans[ki][xi-1])
    n -= 1


