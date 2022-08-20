
for _ in range(int(input())):
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))

    score = 0

    for i in range(k):
        score += int(arr[i] > k)
    print(score)