MOD = 10000000

for _ in range(int(input())):
    def ans():
        n, x, second= map(int, input().split())
        if ( not x and not second) or (x != 0 and second != 0):
            print(-1)
            return
        if x < second: 
            x, second = second, x
        if not((n-1)%x):
            v = 1%MOD
            second =0 
            for i in range(n-1):
                if x == second:
                    second =0
                    v = i+2
                second+=1
                print(v%MOD, end=" ")
            print()
        else:
            print(-1)
    ans()

    