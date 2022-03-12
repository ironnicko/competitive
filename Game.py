for _ in range(int(input())):
    n = int(input())
    A = [int(i) for i in input().split()]
    count = 0
    l = 0
    r = n - 1
    if 0 in A:
        while A[l] == 1: l += 1
        while A[r] == 1: r -= 1
        count = (r+1) - (l-1)
    print(count)
