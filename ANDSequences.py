for test in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    k = a[0]

    for x in a:
        k &= x

    r = a.count(k)
    
    r = r*(r-1) # n c r * 2 

    for i in range(2, len(a)-1): # the factorial function
        r = r*i % ((10e9)+7)
    print(r)