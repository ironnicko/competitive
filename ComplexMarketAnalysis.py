from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print = stdout.write


# Sieve Of Erasthenes
n = 10 ** 6;prime = [True for i in range(n + 1)];prime[1] = False;p = 2
while p * p <= n:
	if prime[p]:
		for i in range(p * p, n + 1, p):prime[i] = False
	p += 1

for _ in range(int(input())):
    n, e = map(int, input().split())
    a = [int(i) for i in input().rstrip().split()]
    ans = 0
    for i in range(n):
        if prime[a[i]]:

            before_e_idx, c = i + e, 0
            while before_e_idx < n and a[before_e_idx] == 1:
                before_e_idx, c = before_e_idx + e, c + 1

            d, after_e_idx = 0, i - e
            while after_e_idx >= 0 and a[after_e_idx] == 1:
                after_e_idx, d = after_e_idx - e, d + 1

            ans += c + d * (c + 1)

    print(f"{ans}\n")