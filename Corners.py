t= int(input())
while t:
    n,m = map(int, input().split())

    arr = [input() for _ in range(n)]
    
    xx = (1, 0, 0, -1, 1, -1, 1, -1)

    yy = (0, -1, 1, 0, 1, -1, -1, 1)

    flag1, flag2 = False, False


    score = 0

    for x in range(n):

        for y in range(m):
            if arr[x][y] == "0":
                flag1 = 1
                for k in range(8):
                    Y = y + yy[k]

                    X = x + xx[k]
                    if X < n and X >= 0 and Y >= 0 and Y < m and arr[X][Y] == '0':
                        flag2 = 1

            else:
                score += 1
    if flag2:
        print(score)


    elif flag1:
        print(score-1)

    else:
        print(score-2)
    t-=1