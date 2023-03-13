for _ in range(int(input())):
    n, x, p = map(int, input().split())

    def solve():
        S = set()
        for i in range(1, min(2*n, p)+1):
            rot = ((i)*(i+1))//2
            cmp1 = (n - x) % n
            if rot % n == cmp1:
               return "Yes"
        return "No"
    print(solve())