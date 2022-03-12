def check(n, m, a):
    for i in range(n-1):
        for j in range(m-1):
            s = sum(map(int, (a[i][j], a[i][j+1], a[i+1][j], a[i+1][j+1])))
            if s == 3:
                print("NO")
                return
    print("YES") 
    
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [[i for i in input()] for _ in range(n)]
    check(n, m, a)