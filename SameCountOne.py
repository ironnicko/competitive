for _ in range(int(input())):
    N, M = map(int, input().split())
    arrays = []
    ONES = 0
    for i in range(N):
        array = list(map(int, input().split()))
        curr_ones = array.count(1)
        ONES += curr_ones
        arrays.append([curr_ones, i+1 ,array])
    arrays.sort()
    if ONES % N:
        print('-1')
    else:
        avg_count = ONES // N
        L = 0
        R = N-1
        ans = []
        while L<R:
            lc, li, la = arrays[L]
            rc, ri, ra = arrays[R]
            if lc == avg_count:
                L += 1
                continue
            if rc == avg_count:
                R -= 1
                continue
            for i in range(M):
                if la[i] == 0 and ra[i] == 1:
                    la[i] = 1
                    ra[i] = 0
                    ans.append([li, ri, i+1])
                    lc += 1
                    rc -= 1
                    arrays[L][0] = lc
                    arrays[R][0] = rc
                    if lc == avg_count:
                        L += 1
                        break
                    if rc == avg_count:
                        R -= 1
                        break
        print(len(ans))
        for row in ans:
            print(*row)
            