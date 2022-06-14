
for _ in range(int(input())):
    n = int(input())
    r = []
    for j in range(n):
        a = input().split()

        for i in range(len(a)):
            a[i] = int(a[i])

        ans = -1

        for i in range(1,len(a)):
            ans = max(ans,a[i]+2-i)

        r.append((ans,a[0]))

    r.sort()

    ans = r[0][0]

    cur = r[0][0]

    for i in range(len(r)):
        if(cur<r[i][0]):
            ans += r[i][0] - cur 
            cur = r[i][0]

        cur += r[i][1]

    print(ans)