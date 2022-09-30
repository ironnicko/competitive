for _ in range(int(input())):
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    sum = a[-1]
    neg = 0

    for i in range(1, n):

        val = neg + i * (a[i] - a[i-1])

        sum -= val

        neg = val

    print(sum)