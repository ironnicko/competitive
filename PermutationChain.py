

m = int(input())

t =0
while t < m:


    M = int(input())
    given_ARR = [i for i in range(1, M+1)]
    print(M)

    MOD = 1e4 + 7

    print(*given_ARR)
    for i in range(M-1):
        given_ARR[i], given_ARR[M-1] = given_ARR[M-1], given_ARR[i]
        print(*given_ARR)

    t += 1