for _ in range(int(input())):
    s = input()
    n = len(s)
    count = set()
    for i in range(n):
        if s[i] not in count:
            count.add(s[i])
        elif s[i] in count:
            n -= 2
            count.clear()
    print(n)