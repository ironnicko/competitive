for _ in range(int(input())):
    n = int(input())
    s = input()

    sum = 0

    res = [0 for _ in range(n)]

    for i in range(n):
        if s[i] == 'L':
            sum += i
        else:
            sum += n - i -1
    i = 0
    j = n- 1

    c= 0
    p=0

    while i < j:
        if s[i] == 'L':
            sum -= i
            sum += n - i - 1
            res[p] = sum
            p+= 1
        i+=1
        if s[i] == "R":
            sum -= n - j - 1
            sum += j
            res[p] = sum
            p+=1
        j-=1

    if p < n:
        for i in range(p, n):
            res[i] = sum
    print(*res)