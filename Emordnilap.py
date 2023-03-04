MOD = int(1e9 + 7)

for _ in range(int(input())):
    n = int(input())
    ans = n * (n-1)
    ans *= ans
    ans %= MOD
    for i in range(1, n-1):
        ans = ((ans * i)) % MOD
    print(ans)
