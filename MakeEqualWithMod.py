for _ in range(int(input())):
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    ones = 0
    con = 0
    prev = a[0]
    for i in a:
        if i == 1:
            ones += 1
        if prev + 1 == i:
            con = 1
        prev = i
    if ones and con:
        print("NO")
    else:
        print("YES")
        