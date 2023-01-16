for _ in range(int(input())):
    n, m = map(int, input().split())
    n <<= 1
    n -= 1
    ans = [0 for _ in range(m)]
    for i in range(n):
        for j, x in enumerate(map(ord, input())):
            ans[j] ^= x
    ans = map(chr, ans)
    print(*ans, sep="")