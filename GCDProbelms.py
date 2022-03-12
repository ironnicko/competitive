from math import gcd
for test in range(int(input())):
    n = int(input())
    a = n-3
    b = 2
    c = 1
    while gcd(a, b) != 1:
        b += 1
        a -= 1
    print(a, b, c)