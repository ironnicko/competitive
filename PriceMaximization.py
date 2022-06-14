from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print =lambda x : stdout.write(str(x)+"\n")

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        ans, a[i] = ans + a[i]//k, a[i]%k
    a.sort()

    i = 0
    j = n - 1
    while j - i >= 1:
        if not(a[i] + a[j] < k):
            ans += 1
            j -= 1
        i += 1
    print(ans)