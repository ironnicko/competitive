for _ in range(int(input())):
    n = int(input())
    sum = 0
    s = input()
    first = int(s[0])
    ans = []

    for i in range(1, n):
        if not first:
            ans.append("+")
            first += int(s[i])
        else:
            ans.append("-")
            first -= int(s[i])
    print(*ans, sep="")
