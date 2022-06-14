from sys import stdin

input = stdin.readline
for _ in range(int(input())):
    n = int(input())
    
    arr = [int(x) for x in input().split()]
    i = 0
    k = n-1
    a = arr[0]
    b = arr[-1]
    ans = 0
    while i < k:
        if a == b:
            ans = i+1+(n-k)
        if a >= b:
            k-=1
            b += arr[k]
        else:
            i+=1
            a += arr[i]
    print(ans)