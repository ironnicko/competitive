from collections import Counter

for _ in range(int(input())):
    n = int(input()) % int(1e5+1)

    List = list(map(int, input().split()))
    numbers = Counter(List)

    ans = 1
    idx = 1

    for i in numbers:
        if numbers[i] > 1:
            ans = idx
            break
        idx += 1

    print(ans, n)
