def primeFactors(x):
    count = 0
    for i in range(15):
        if x//2 == x/2:
            x = x//2
            count += 1
        else:
            return count
    return count

n = int(input())
a = [int(i) for i in input().split()]
for i in a:
    ans = 0
    if i%2:
        ans += 1
    elif i == 0:
        print(0, end=" ")
        continue
    main = primeFactors(i+1 if i%2 else i)
    ans += min(15-main, 32768-i)
    print(ans, end=" ")