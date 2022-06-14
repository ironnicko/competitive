for _ in range(int(input())):
    s = input()
    n = len(s)
    a = 0
    b = 0 
    idx = None
    f = 1
    if n == 1 or 'B' not in s or 'A' not in s or s[-1] != 'B':
        print("NO")
        continue
    else:
        for i in range(n):
            if s[i] == 'A':
                a +=1
            else:
                b += 1
                if b > a:
                    print("NO")
                    f = 0
                    break
    if f:
        print("YES")
