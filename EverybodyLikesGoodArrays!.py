for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    c = arr[0] & 1
    final = 0
    for i in range(1, n):
        if c == arr[i] & 1:
            final += 1
        else:
            c ^= 1
    print(final)