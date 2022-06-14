from collections import Counter
for _ in range(int(input())):
    n = int(input())
    array = [int(i) for i in input().split()]
    count = Counter(array)
    freq = count.most_common(1)[0][1]
    start = n - freq
    ans = 0 
    while start > 0:
        ans += min(freq, start) + 1
        start -= freq
        freq *= 2
    print(ans)
