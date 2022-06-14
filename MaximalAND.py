def andFind(a : list):
    andRes = a.pop(0)    
    for i in a:
        andRes &= i
    return andRes
for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = None
    a = sorted([int(i) for i in input().split()])
    if n > k:
        set_bit = len(bin(a[-1])) - 2
        for i in range(n):
            a[i] |= set_bit
    else:
        for i in range(30):
            a[0] |= 1<<i
        ans = a[0]
    if ans != None:
        print(ans)
    else:
        print(andFind(a))