from math import gcd


for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    f = 0

    S = set()
    for i in range(n):
        if f == 1 or f == 2:
            break
        for j in range(i+1, n):
            f = gcd(arr[i], arr[j])
            if f == 1 or f == 2:
                S.update({i, j})
                break
    if f > 2:
        print("No")
    elif f == 1:
        print("Yes")
    else:
        start = 2
        total = set(i for i in range(n))
        for i in (total - S):
            S.add(i)
            f = gcd(f, arr[i])
            start += 1
        print(("No", "Yes")[start == n])