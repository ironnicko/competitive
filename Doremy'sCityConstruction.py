from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = sorted(map(int, input().split()))
    ans = n//2

    for i in range(1, n):
        if arr[i] != arr[i-1]:
            ans = max(ans, i * (n-i))
    print(ans)
