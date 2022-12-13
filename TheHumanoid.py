from sys import setrecursionlimit


def recurr(n, arr, idx, g, b, h):
    if idx >= n:
        return 0

    if h > arr[idx]:
        return recurr(n, arr, idx+1, g, b, h+(arr[idx]//2))+1
    else:
        take_b, take_g = 0, 0
        if b:
            take_b = recurr(n, arr, idx, g, b-1, h*3)
        if g:
            take_g = recurr(n, arr, idx, g-1, b, h*2)
        return max(take_b, take_g)


for _ in range(int(input())):

    n, h = map(int, input().split())
    setrecursionlimit(max(n+1, int(1e4)))
    arr = sorted(map(int, input().split()))
    ans = recurr(n, arr, 0, 2, 1, h)
    print(ans)
