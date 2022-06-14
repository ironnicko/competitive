for _ in range(int(input())):
    n = int(input())
    s = input()
    main = 0
    for i in range(n-1):
        if s[i] == '1':
            if 0 < i < n-1:
                if s[i-1] == '0' and s[i+1] == "0":
                    main += 1
        if s[i] == s[i+1] == '0':
            main += 2
    print(main)
