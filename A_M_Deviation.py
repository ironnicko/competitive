testCase = int(input())
while testCase > 0:
    testCase -= 1
    a1, a2, a3 = map(int, input().split())

    if (a1 + a2 + a3) % 3 == 0:
        print(0)
    else:
        print(1)