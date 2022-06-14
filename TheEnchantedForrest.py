from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print = stdout.write

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    if k < n:
        score = sum(a[:k])
        mx = int(score)
        for i in range(k, n):
            score -= a[i-k]
            score += a[i]
            mx = max(score, mx)
        ans = mx + k*(k-1)//2
        print(f"{ans}\n")
    else:
        ans = sum(a) + ((n-1)*n)//2 + n*(k-n)
        print(f"{ans}\n")