def check(i):
    temp = 0
    if i & 1:
        while i & 1:
            i //= 2
            temp += 1
        return temp
    else:
        while (i & 1) == 0:
            i //= 2
            temp += 1
        return temp

for _ in range(int(input())):
    n = int(input())

    arr = sorted(map(int, input().split()))
    par = [0, 0]
    ans = [float('inf'), float('inf')]

    for i in arr:
        par[i&1] += i
    for i in arr:
        ans[i&1] = min(ans[i&1], check(i))
    
    if par[1] & 1:
        if not ans[1] and ans[0]:
            print(ans[0])
        elif not ans[0] and ans[1]:
            print(ans[1])
        else:
            print(min(ans))
    else:
        print(0)
        