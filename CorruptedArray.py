 
for _ in range(int(input())):
    n=int(input())
    A=[int(i) for i in input().split()]
    A.sort()
    S=sum(A)
    if S-A[-1]-A[-2]==A[-2]:
        print(*A[:-2])
    else:
        r=S-A[-1]
        for i in range(n+1):
            if r-A[i]==A[-1]:
                ans=(A[:i]+A[i+1:-1])
                print(*ans)
                break
        else:
            print(-1)