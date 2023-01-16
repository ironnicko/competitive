from collections import Counter
for _ in range(int(input())):
    n = int(input())
    count = Counter()
    arr = []
    for __ in range(n):
        ___, *others = map(int, input().split())
        count.update(others)
        arr.append(others)
    cnt = 0
    for i in arr:
        cnt += int(any(count[j] == 1 for j in i))
    print(("No", "Yes")[cnt != n])
