for _ in range(int(input())):
    s = input()
    n = len(s)

    print(s[0], end=" ")

    if s[0] == s[-1]:
        print(s[1:n-1], s[-1])
    else:
        if s[1] == 'a':
            print(s[1:2], s[2:])
        else:
            print(s[1 : n - 2], s[n-2:])
            