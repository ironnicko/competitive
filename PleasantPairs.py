for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]

    res = 0
    for i in range(n):
        for j in range(arr[i]-i-2, n, arr[i]):
            if arr[i]*arr[j] == i+j+2 and i < j:
                res += 1
    
    print(res)