for _ in range(int(input())):
    n = int(input())
    s=  input()
    z = s.count('0')
    o = s.count('1')

    if z == 0:
        print(n, 0)
        continue
    if o == 0:
        print(n, 0)
        continue
    print(1, abs(z-o)+1)
    q = 0
    for i in range(abs(z-o)):

        t = ""
        for j in range(len(s)-1):

            if (s[j] == '0' and s[j+1] == '1') or (s[j] == '1' and s[j+1] == '0'):
                q = j
                break
        print(q+1, q+2, int(z>o))
        for j in range(len(s)):
            if j != q and j != q+1:
                t += s[j]
            elif j == q:
                t += chr(int(z > o) + 48)
        s = t

    print(1, len(s), 0)