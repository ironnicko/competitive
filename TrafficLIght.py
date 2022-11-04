for _ in range(int(input())):
    n, c = input().split()
    n = int(n)
    s = input()
    g_idx = []
    for i in range(n):
        if s[i] == 'g':
            g_idx.append(i)
    score = 0
    for i in range(n):
        if s[i] == c:
            temp = []
            for j in g_idx:
                if j < i:
                    temp.append(n - abs(i-j))
                else:
                    temp.append(abs(i-j))
            item = min(temp) if temp else 0
            score = max(item, score)
    print(score)
