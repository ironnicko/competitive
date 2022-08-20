from collections import Counter

for _ in range(int(input())):
    n = int(input())

    count = Counter(input().split())

    print(max( 2 * count.most_common(1)[0][1]- n, n & 1))