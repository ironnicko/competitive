from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    count = Counter()
    total = 0
    for idx in range(n):
        if a[idx] >= idx+1:
            a[idx] = -1
        if a[idx] > 1:
            count[a[idx]] += 1
            total += 1
    score = 0
    for idx in range(n):
        if count.get(idx+1, 'a') != 'a':
            total -= count[idx+1]
        if idx+1 > a[idx] and a[idx] != -1:
            score += total
        if count.get(0, -2) != -2:
            total -= count[0]
            count[0] = -2
    print(score)