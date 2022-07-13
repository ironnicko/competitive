for _ in range(int(input())):
    a = [list(map(int, input().split())) for _ in range(2)]
    cnt = 0
    for i in range(2):
        for j in range(2):
            if a[i][j]:
                cnt += 1
    if cnt == 0:
        print(0)
    elif cnt <= 3:
        print(1)
    else:
        print(2)