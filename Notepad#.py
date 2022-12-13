for _ in range(int(input())):
    n = int(input())
    s = input()
    f = 1
    for i in range(n-2):
        if s[i: i+2] in s[i+2:]:
            f = 0
            break
    print(("YES", "NO")[f])
