from math import log2, floor, ceil
def isPow2(num):
    if num == 0:
        return False
    else:
        return ceil(log2(num)) == floor(log2(num))

for _ in range(int(input())):
    s = input()
    ans = float('inf')
    if isPow2(int(s)):
        print(0)
    else:
        for i in range(60):
            sn = str(2**i)
            ok = False
            c, j, k = 0, 0, 0
            while (j!=len(s) and k!=len(sn)):
                if s[j] == sn[k]:
                    j += 1
                    k += 1
                    ok = True
                else:
                    j += 1
                    c += 1
                    ok = False
            if ok:
                if j == len(s):
                    k -= 1
                    c += len(sn) - k - 1
                elif k == len(sn):
                    j -= 1
                    c += len(s) - j - 1
            else:
                k -= 1
                c += len(sn) - k - 1
            if c == 1:
                ans = 1
                break
            else:
                ans = min(ans, c)
        print(ans)