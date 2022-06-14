a=int(input())
for r in range(a):
    b=int(input())
    c=[int(x) for x in input().split()]
    if sum(c)%b==0:
        print(0)
    else:
        print(1)