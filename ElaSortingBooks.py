def miis():
    return map(int, input().split())
        
for _ in range(int(input())):
    n, k = miis()
    s = list(input())
    a = [0 for i in range(26)]
    for i in s:
        a[ord(i)-ord('a')] += 1
    debt = 0
    for i in range(k):
        need = n//k-debt
        for j in range(26):
            if need == 0:
                break
            if a[j] == 0:
                break
            a[j] -= 1
            need -= 1
        print(chr(j+ord('a')), end='')
        debt += need
    print()
