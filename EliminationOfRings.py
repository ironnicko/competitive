from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = Counter(arr)
    if len(count) > 2:
        print(n)
    elif len(count) & 1 == 0:
        print(n//2 + 1)
    else:
        print(1)
