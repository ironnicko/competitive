for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        freq = [0 for _ in range(10)]

        mx, uni = 0, 0

        for j in range(i, n):
            if freq[int(s[j])]+1 > 10:
                break
            freq[int(s[j])]+=1
            mx = max(mx, freq[int(s[j])])
            uni +=  int(freq[int(s[j])] == 1)
            if uni >= mx: ans += 1
    print(ans)