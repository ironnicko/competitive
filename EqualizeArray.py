from collections import Counter

for _ in range(int(input())):
    n = int(input())
    values = sorted(Counter(map(int, input().split())).values())
    ans, temp = 0, 0
    for i in range(len(values)):
        temp = (len(values) - i) * (values[i])
        ans = max(ans, temp)

    print(n - ans)
