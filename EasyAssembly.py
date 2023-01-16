from collections import defaultdict

SET = set()
blocks = []
n = int(input())
for _ in range(n):
    l, *rest = list(map(int, input().split()))
    SET.update(rest)
    blocks.append([l]+rest)

SET = sorted(SET)
next = defaultdict(int)

for i in range(len(SET)-1):
    next[SET[i]] = SET[i+1]

s = 0
c = 0

for block in blocks:
    length_of_segment, *rest = block
    for i in range(length_of_segment-1):
        if rest[i+1] != next[rest[i]]:
            s += 1

print(s, n + s - 1)