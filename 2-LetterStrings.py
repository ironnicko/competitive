from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = [input() for _ in range(n)]
    d = Counter(s)
    l = list(d.keys())
    count = 0
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i][0] == l[j][0] and l[i][1] == l[j][1]:
                pass
            elif l[i][0] == l[j][0] or l[i][1] == l[j][1]:
                count += d[l[j]] * d[l[i]]
    print(count)
