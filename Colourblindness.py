
MOD = 100000000

for _ in range(int(input()) % MOD):
    Number = int(input())

    Array  = [input() for _ in range(2)]
    Flag = "YES"
    for i in range(Number):
        if Array[1][i] != Array[0][i]:
            Flag = "NO"
        if (Array[1][i] == "B" and Array[0][i] == "G") or (Array[1][i] == "G" and Array[0][i] == "B"):
            Flag = "YES"
        if Flag == "NO":
            break
    print(Flag)