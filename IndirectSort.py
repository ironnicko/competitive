for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(("NO", "YES")[arr[0] == 1])