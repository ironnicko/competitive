for _ in range(int(input())):
    n = int(input())
    a  = [int(i) for i in input().split()]
    diff = float('-inf')
    idx = 0
    for i in range(n-2, -1, -1):
        diff = max(a[i] - a[i-1], diff)
        idx = i
    