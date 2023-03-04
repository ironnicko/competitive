from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = input().split()

    final = sorted(s)
    f = 1
    vis = set()
    n = len(s)

    for i in range(n):
        if len(vis) == n:
            break
        f = 0
        if i in vis:
            continue
        vis.add(i)
        for j in range(n):
            if j in vis:
                continue
            if s[i] == s[j][::-1] and j not in vis:
                f = 1
                vis.add(j)
                break
        if not f:
            break

    print(("NO", "YES")[f])