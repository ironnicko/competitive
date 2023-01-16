for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    final1 = arr[0]
    final2 = arr[0]
    for i in range(1, n):
        final1 = final1 | arr[i]
        final2 = final2 & arr[i]
    print(final1 - final2)
