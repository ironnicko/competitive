from sys import stdin,stdout
input = stdin.readline
print = stdout.write

a =input().rstrip().lower();b =input().rstrip().lower();print(str((a>b) - (a<b)))