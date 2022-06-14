from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print = lambda x : stdout.write(str(x)+"\n")

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())
    cnt = 0
    res = 0
    flag1, flag2 = 1, 1
    one_S = -1
    one_E = -1
    for i in range(n):
        if s[i] == "1" and flag1:
            one_S = i
            flag1 = 0
        if s[~i] == "1" and flag2:
            one_E = n+~i
            flag2 = 0
        if not(flag1 or flag2):
            break
    if one_S == -1:
        print(0)
        continue
    elif one_S != n-1:
        if k >= n - one_E - 1: # if the last "1" is at a distance less than "k" from end.
            s[one_E], s[n-1] = s[n-1], s[one_E]
            k -= n-one_E-1
            if k >= one_S: # if the first "1" is at a distance "k" or greater from the start.
                s[one_S], s[0] = s[0], s[one_S]
        elif k >= one_S: # if the first "1" is at a distance "k" or greater from the start.
            s[one_S], s[0] = s[0], s[one_S]
    for i in range(n-1):
        tmp = int(s[i]+s[i+1])
        res += tmp
    print(res)