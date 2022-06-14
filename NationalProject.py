for _ in range(int(input())):
    n, g, b = map(int, input().split())
    CONST = (n+1)//2
    final = (CONST//g) * (g+b)
    final += -b if final%g==0 else CONST%g
    print(max(n, final))