
for _ in range(int(input())):
    n = int(input())
    arr = [-1] + list(map(int, input().split()))
    pref = [0 for _ in range(n+1)]
    pref[0] = 1
    for i in range(1, n+1):
        if i + arr[i] <= n and pref[i-1]:
            pref[i + arr[i]] = 1
        if i - arr[i] - 1 > -1 and pref[i - arr[i] - 1]:
            pref[i] = 1
    print(("NO", "YES")[pref[n]])