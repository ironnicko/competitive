for _ in range(int(input())):
    n = int(input())

    final = [0 for _ in range(n)]
    parity = n
    for i in range(1, n, 2):
        final[i] = parity
        parity -= 1
    for i in range(0, n, 2):
        final[i] = parity
        parity -= 1
    print(*final)