# need to prioritse the defense first then satisfy the attack

for _ in range(int(input())):
    a = sorted([int(i) for i in input().split()], reverse=1)
    n = int(input())

    while n:
        x,y = map(int, input().split())
        

        n-=1