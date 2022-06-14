from sys import stdin, stdout

n = int(stdin.readline())# number of stairs to reach the top
m = int(stdin.readline())# max you can skip

def CountWays(n, m):
    #Base Case
    if n <= 1:
        return n
    res = 0
    i = 1
    while i<= m and i <= n:
        res = res + CountWays(n-i, m)
        i += 1
    return res
print(CountWays(n+1, m))