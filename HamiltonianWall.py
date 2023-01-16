for _ in range(int(input())):
    n = int(input())
    A = [[0 for __ in range(n)] for _ in range(2)]
    B = [list(input()) for _ in range(2)]
    row = 0
    for i in range(2):
        for j in range(n):
            A[i][j] = int(B[i][j] == 'B')
            B[i][j] = A[i][j]

    def func(row, pred, flag):
        i = 0
        while i < n - 1:
            if pred[row][i]:
                pred[row][i] = 0
                pos = 1 if not row else -1
                if not pred[row][i + 1] and not pred[row + pos][i]:
                    flag = 0
                    break
                elif not pred[row][i + 1] and pred[row + pos][i]:
                    row ^= 1
                    i -= 1
                elif pred[row][i + 1] and pred[row + pos][i]:
                    row ^= 1
                    i -= 1
            else:
                flag = 0
            i += 1
        return flag

    f1 = func(0, A, 1)
    f2 = func(1, B, 1)

    print(("NO", "YES")[f1 or f2])
