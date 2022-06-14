n = int(input())
a = [int(i) for i in input().rstrip().split()]
ans = 0
f1, f2 = 1, 1
for i in range(n):
    if a[i] == max(a) and f1:
        maxi = i
        f1 = 0
    if a[n-i-1] == min(a) and f2:
        mini = n-i-1
        f2 = 0
if maxi > mini:
    ans -= 1
ans += maxi + (n - mini -1)
print(ans)
