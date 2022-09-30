for _ in range(int(input())):
    n = int(input())
    ath = [list(map(int, input().split())) for _ in range(n)]
    def comp(i, gold):
        count = 0
        for j in range(5):
            count += int(ath[i][j] < ath[gold][j])
        return count > 2
    gold = 0

    for i in range(1, n):
        if comp(i, gold):
            gold = i

    for i in range(n):
        if i == gold: continue
        if comp(i, gold):
            gold = -1
            break
    print(gold + int(gold != -1))