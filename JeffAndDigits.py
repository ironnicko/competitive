n = int(input())
f =1
a = sorted([i for i in input().split()])
for i in range(n, 0, -1):
    number = int("".join(a[:i][::-1]))
    if not(number%90):
        f = 0
        break
if f:
    if '0' in a:
        print(0)
    else:
        print(-1)
else:
    print(number)