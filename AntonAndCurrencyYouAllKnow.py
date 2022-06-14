from sys import stdin,stdout
input = stdin.readline
print = stdout.write

n = list(input().rstrip())
main = []
f=1
for i in range(len(n)):
    if not(int(n[i])&1):
        main.append(i)
if not(len(main)):
    print(str(-1))
    f=2
if f != 2:
    for i in main:
        if n[-1] > n[i]:
            n[-1], n[i] = n[i], n[-1]
            f = 0
            break
if f and f!=2:
    n[main[-1]], n[-1] = n[-1], n[main[-1]]
    print("".join(n))
elif f==2:
    pass
else:
    print("".join(n))