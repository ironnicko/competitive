from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    s = input().rstrip()
    ans = 9
    for __ in range(2):
        cnt0 = 0
        cnt1 = 0
        for i in range(0,10):
            if (i % 2 == 0) :
                cnt0 += s[i] != ('0' if __ == 0 else '1')
            else:
                cnt1 += s[i] == ('1' if __ == 0 else '0')
            if (cnt0 > cnt1 + (10 - i) / 2):
                ans = min(ans, i)
            if (cnt1 > cnt0 + (9 - i) / 2) :
                ans = min(ans, i)

    print(str(ans+1)+"\n")