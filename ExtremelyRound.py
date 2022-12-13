from math import log10, ceil
for _ in range(int(input())):
    n = int(input())

    l = int(log10(n) + 1)

    s = str(n)

    first = int(s[0])
    print(first + 9*l - 9)
