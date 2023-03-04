from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    current = int(n)
    big = 1
    hash = defaultdict(int)
    i = 2
    while i * i <= n:
        if not (current % i):
            cnt = 0
            while not (current % i):
                cnt += 1
                current //= i
            hash[i] = cnt
            big = max(big, cnt)
        i+=1

    if current != 1:
        hash[current] = 1
    final = -1
    for i in range(big, -1, -1):
        inhere = 1
        for j in hash:
            if hash[j]:
                hash[j] -= 1
                inhere *= j
        final += inhere
    print(final)
