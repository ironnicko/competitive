for _ in range(int(input())):
    n = int(input())
    if n < 3:
        print(n)
    else:
        s = ""
        j = n%3 or 1
        s = str(j)
        n -= j
        while n > 0:
            if s[-1] == '1':
                s += '2'
                n -= 2
            else:
                s += '1'
                n -= 1
        print(s) if int(s[::-1]) < int(s) else print(s[::-1])

