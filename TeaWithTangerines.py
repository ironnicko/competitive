for _ in range(int(input())):
    n = int(input())
    n%=1000
    score = 0
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    for i in range(1, n):
        if (arr[i] + 2*arr[0]-2)//(2*arr[0]-1) > 1:
            score += (arr[i] + 2 * arr[0] - 2)//(2*arr[0]-1)
            score -= 1
    print(score)