for _ in range(int(input())):
    n = int(input())
    l = [1]+list(map(int, input().split()))
    s = list(input())
    q = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        if s[i] == 'B':
            q[i] -= 1
        else:
            q[i] += 1
        q[l[i]-1] += q[i]
    print(q.count(0))
