from bisect import bisect_right
from collections import Counter
n = int(input())

a = sorted([int(i) for i in input().split()])

count = Counter(a)

if a[-1]> 2 *(a[0]):
    first = bisect_right(a, 2 * (a[0]))
    second = n - bisect_right(a, a[-1]//2)
    c = min(first, second)
    print(c-1)
else:print(0)