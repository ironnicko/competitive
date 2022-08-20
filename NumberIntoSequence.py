def prime_factor(n):
    i = 2
    prime = []
    while i*i <= n:
        if n % i == 0:
            prime.append(i)
            prime += prime_factor(n//i)
            break
        i += 1
    if prime: return prime
    else: return [n]

t = int(input())
while t:
    n = int(input())
    
    pfactor = prime_factor(n)
    primes = list(set(pfactor))
    ptimes = []
    for elem in primes:
        ptimes.append(pfactor.count(elem))

    maxPrime = primes[ptimes.index(max(ptimes))]
    maxTimes = max(ptimes) - 1
    other = 1
    for i in range(len(pfactor)):
        if maxPrime != pfactor[i]:
            other *= pfactor[i]
    
    ans = [maxPrime]*maxTimes + [maxPrime * other]
    print(len(ans))
    print(*ans)
    t -= 1