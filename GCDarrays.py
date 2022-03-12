testCase = int(input())
while testCase > 0:
    testCase -= 1
    l, r, k = input().split()
    l, r, k = int(l), int(r), int(k)

    if l == r:
        if l > 1:
            print("YES")
        else:
            print('NO')
    else:
        odd, even = (r - l + 1) // 2, (r - l + 1) // 2
        if r % 2 == l % 2:
            if r % 2 == 1:
                odd += 1
            else:
                even += 1
        if k >= odd:
            print("YES")
        else:
            print("NO")