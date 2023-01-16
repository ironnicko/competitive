MOD = 998244353

for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = 0
    temp = 1
    for i in range(1, n):
        if s[i] == s[i-1]:
            temp = (temp * 2) % MOD
        else:
            temp = 1
        ans = (ans + temp) % MOD

    print(ans + 1)
