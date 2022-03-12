for _ in range( int(input()) ):
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    for  i in  range(n):
        ans = max(ans, a[i] -i -1)
    print(ans)