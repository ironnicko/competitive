for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    comp = lambda x : x[1]
    resultant = sorted([[a[i], b[i]] for i in range(n)], key=comp)
    estimated = 0
    for i in range(n-1):
        estimated += resultant[i][0]
        resultant[i+1][0] += resultant[i][1]
    estimated += resultant[n-1][0]
    print(estimated)