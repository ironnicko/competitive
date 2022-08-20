for _ in range(int(input())):
    n = int(input())
    s = [input() for _ in range(n)]
    S = set(s)
    b = ""
    for t in s:
        for i in range(len(t)-1):
            if t[:i+1] in S and t[i+1:] in S:
                b += '1'
                break
        else:
            b += '0'
    print(b)