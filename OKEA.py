testCase = int(input())
while testCase>0:
    testCase -= 1
    n, k = map(int, input().split())
    if n%2 == 1:
        if k == 1:
            print("YES")
            for i in range(1, n+1):
                print(i)
        else:
            print("NO")
    else:
        print("YES")
        for i in range(1, n+1):
            sum = i
            for j in range(1, k+1):
                print(sum, end=" ")
                sum += n