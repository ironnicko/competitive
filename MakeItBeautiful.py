
for _ in range(int(input())):
    n = int(input())
    arr = sorted(map(int, input().split()), reverse=1)
    if arr[0] == arr[-1]:
        print("NO")
    else:
        ans = "YES"
        for i in range(1, n):
            if arr[i] != arr[i-1]:
                arr[i], arr[0] = arr[0], arr[i]
        print(ans)
        if ans == 'YES':
            print(*arr)
