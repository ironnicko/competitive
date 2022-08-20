
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    res = sorted(a)
    print(res[n-1] + res[n-2] - res[0] - res[1])