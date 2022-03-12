testCase = int(input())
while testCase > 0:
    testCase -= 1
    L = int(input())
    A = [int(i) for i in input().split()]

    case = A[1:L-1]
    ans = 0

    if L == 3 and A[1]%2:
        print(-1)
        continue
    if len(set(case)) == 1 and case[0]==1:
        print(-1)
        continue
    else:
        for i in case:
            ans += (i+1)//2
        print(ans)