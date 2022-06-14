from sys import stdin,stdout
input = stdin.readline
print = stdout.write

n = int(input())
main = (0, 0)
n1 = [int(i) for i in input().rstrip().split()]
n2 = [int(i) for i in input().rstrip().split()]
for i in range(n):
    new = (max(main[0], main[1] + n1[i]), max(main[1], main[0] + n2[i]))
    main = new
print("%i"%(max(main)))