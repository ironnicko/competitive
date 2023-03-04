from collections import deque

for _ in range(int(input())):

    n = int(input())

    de = deque(maxlen=n)

    for i in list(map(int, input().split())):
        de.append(i)
        while next(iter(de)) < len(de):
            de.popleft()
        print(len(de), end=" ")
    print()