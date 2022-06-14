from sys import stdin
input = stdin.readline
s="0123456789"
n=int(input())
for i in s[:n]+s[n::-1]:
    a=int(i)
    print(" ".join(" "*(n-a)+s[:a]+s[a::-1]))