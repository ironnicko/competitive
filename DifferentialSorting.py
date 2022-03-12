for _ in range(int(input())):
    N = int(input())
    A = [int(i) for i in input().split()]
    if A[-2] > A[-1]:
        print(-1)
        continue
    elif A[-1]<0:
        if A == sorted(A):
            print(0)
        else:
            print(-1)
        continue
    print(N-2)
    for i in range(1, N-1):
        print(i, N-1, N, sep=" ")
