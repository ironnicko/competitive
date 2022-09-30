
s=input()
t=input()
ans=0
for i in range(1, len(s)+1):
    i = max(i,1)
    if len(s)%i==len(t)%i==0:
        ans+= (t[:i]==s[:i] and s==(len(s)//i)*s[:i] and t==(len(t)//i)*t[:i])
print(ans)