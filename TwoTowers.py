
for _ in range(int(input())):
    n, m = map(int, input().split())
    n,m = n%int(1e9), m%int(1e9)
    n += m
    s1 = input() + input()[::-1]
    string = 0
    for i in range(n-1):
        if s1[i] == s1[i+1]:
            string += 1
    if string  >= 2:
        print("NO")
        continue
    print("YES")