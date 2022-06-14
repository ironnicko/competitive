from collections import Counter
from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n, k = map(int, input().rstrip().split())
    s = input().rstrip()
    count = Counter(s)
    pairs, odd = 0, 0
    for i in count.values():
        pairs += i//2
        odd += i % 2
    ans = 2 * (pairs//k)
    odd += 2 * (pairs%k)
    print(str(ans)+'\n') if odd < k else print(str(ans+1)+'\n')