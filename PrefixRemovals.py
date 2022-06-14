for _ in range(int(input())):
    s=input()
    sen=len(set(list(s)))
    if sen==1:
        print(s[-1])
    else:
        f=0
        for i in range(len(s)-1):
            if s[i] not in s[i+1:]:
                f=i
                break
        print(s[f:])