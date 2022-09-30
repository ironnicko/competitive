
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    ans = "YES"

    for i in range(n):
        if a[i]>b[i] or b[i]-b[(i+1)%n]>1 and b[i]!=a[i]:
            ans= "NO"
    print(ans)
