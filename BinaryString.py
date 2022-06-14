from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    s = input().rstrip()
    l, r = 0, 0
    z, ones = 0, s.count('1')
    mi = 10e9
    while 1:
        mi = min(mi, max(ones,z))
        if ones >= z:
            if r == len(s):
                break
            if s[r] == '1':
                ones -= 1
            else:
                z += 1
            r += 1
        else:
            if s[l] == '1':
                ones += 1
            else:
                z -= 1
            l += 1
    print(str(mi)+"\n")