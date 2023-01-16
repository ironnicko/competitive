"""
    Competitve Programming : Nikhil
"""

for _ in range(int(input())):
    n, l = map(int, input().split())
    arr = list(map(int, input().split()))

    s1, s2 = 1, 1
    c1, c2 = 0, l
    TIME = 0
    i = 0
    j = n-1
    while i <= j:
        t1 = (arr[i] - c1) / s1
        t2 = (c2 - arr[j]) / s2

        if t1 <= t2:
            TIME += t1
            c1 += s1 * t1
            c2 -= s2 * t1
            s1 += 1
            i += 1
        else:
            TIME += t2
            c1 += s1 * t2
            c2 -= s2 * t2
            s2 += 1
            j -= 1
    ans = (c2 - c1) / (s1 + s2) + TIME
    print(f"{ans:.15f}")
