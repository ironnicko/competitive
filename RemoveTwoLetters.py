for _ in range(int(input())):
    n = int(input())
    s = input()

    c = 0

    for i in range(0, n-2):
        c += int(s[i] == s[i+2])

    print(n - 1 - c)
