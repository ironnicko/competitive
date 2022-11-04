for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    final = []

    if n == k:
        final.append(arr[0])
    if k == 1:
        print("YES")
        continue
    for i in range(1, k):
        final.append(arr[i] - arr[i-1])
    if arr[0] > final[0] * (n - k + 1):
        print("NO")
        continue


    print(("NO", "YES")[final == sorted(final)])