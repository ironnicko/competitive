t=int(input())
while(t>0):
        n=input();l=n[0]
        if(len(n)==1):
                k=False
        else:
                k=True
        for i in range(1,len(n)):
                if(n[i]==n[i-1]):
                        l+=n[i]
                else:
                        if(len(l)<2):
                                k=False
                                break
                        l=n[i]
        if(len(l)==1):
                k=False
        if(k==True):
                print('YES')
        else:
                print('NO')
        t-=1
