testCase = int(input())
while testCase > 0:
    testCase -= 1
    n, k = input().split()
    n, k = int(n), int(k)
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    while n > 0:
        n -= 1
        if A[n] <= k:
            k += B[n]
            B.pop(n)
            A.pop(n)
            n = len(A)
            continue
    print(k)