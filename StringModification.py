
for _ in range(int(input())):
    l=[]
    n=int(input())
    s=input()
    for i in range(1,n+1):
        if((n-i+1)%2 and i>=2):
            l.append((s[i-1:]+s[i-2::-1],i))
        elif((n-i+1)%2):
            l.append((s,i))
        else:
            l.append((s[i-1:]+s[:i-1],i))

    print(min(l)[0])
    print(min(l)[1])