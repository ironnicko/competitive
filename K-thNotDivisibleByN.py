for _ in range(int(input())):
    n, k = map(int, input().split())
    if k < n:
        result = k
    else:
        result = (k // (n-1))  * n
        rem = k % (n-1)
        result += rem if rem != 0 else -1
    print(result)