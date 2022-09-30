from collections import Counter
from math import gcd
for _ in range(int(input())):
    input()
    dic = Counter()
    a,b = 0, 0
    ans = []

    for i in input():
        a += int(i == 'D')
        b += int(i == 'K')
        GCD = max(1, gcd(a,b))
        pair = (a//GCD, b//GCD)
        dic[pair]+=1
        ans.append(dic[pair])
    print(*ans)