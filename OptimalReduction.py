
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    m = float('-inf')

    idx= -1
    for i in range(n):

        idx = idx if a[i] < m else i
        m = max(m, a[i])
    ans = "YES"
    for i in range(idx, n-1):
        if a[i] < a[i+1]:
            ans = "NO"
    for i in range(idx, 0, -1):
        if a[i] < a[i-1]:
            ans = "NO"

    print(ans)