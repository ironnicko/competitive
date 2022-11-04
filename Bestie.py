from math import gcd
MOD = 200
for _ in range(int(input())):
    n = int(input())
    n %= MOD
    arr = list(map(int, input().split()))
    main = gcd(*arr)
    if main == 1:
        print(0)
    else:
        for i in range(n-1, -1, -1):
            cond = gcd(main, gcd(arr[i], i+1)) == 1
            if cond:
                print(min(3, n - i))
                break
