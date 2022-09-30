from collections import Counter
MOD  = 10000
for _ in range(int(input()) % MOD):
    n = input()
    word = input()
    ans = "YES"
    permutation = Counter("Trumi")
    word = Counter(word)
    if permutation != word: ans = "NO"
    print(ans)