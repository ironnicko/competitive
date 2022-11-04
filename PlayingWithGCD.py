from math import gcd

for _ in range(int(input())):
    n = int(input())
    arr = [-1] + list(map(int, input().split()))
    b = [0 for _ in range(n+1)]
    if n == 1:
        print("YES")
        continue
    b[0] = arr[1]
    b[n] = arr[n]
    ans = "YES"
    for i in range(1, n):
        b[i] = arr[i] * arr[i+1] // gcd(arr[i], arr[i + 1])
    for i in range(1, n+1):
        if gcd(b[i], b[i-1]) != arr[i]:
            ans = "NO"
            break
    print(ans)