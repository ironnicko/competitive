from math import ceil
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted([int(i) for i in input().split()])
    hash = {}
    ans = float('-inf')
    p2 = n-1
    for i in range(n+1//2):
        if p2 >= i:
            if a[i]%k:
                util = ceil(a[i]/k)
                formula = (util * k) - a[i]
                hash[formula] = hash.get(formula, 0)+1
                formula = ((util+(hash[formula] - 1))*k) - a[i]
                ans = max(ans, formula+1)
            if a[p2]%k and p2 != i:
                util2 = ceil(a[p2]/k)
                formula2 = (util2 * k) - a[p2]
                hash[formula2] = hash.get(formula2, 0)+1
                formula2 = ((util2+(hash[formula2] - 1))*k) - a[p2]
                ans = max(ans, formula2+1)
        p2 -= 1

    print(ans) if ans != float('-inf') else print(0)
