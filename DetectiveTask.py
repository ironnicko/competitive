for _ in range(int(input())):
    s = input()
    one = -1
    zero = -1
    for i in range(len(s)):
        if(s[i]=='1'):one = i
        elif(s[i]=='0'):
            zero = i
            break
    if(one == -1 and zero == -1):
        print(len(s))
    elif(one == -1):
        print(zero+1)
    elif(zero == -1):
        print(len(s)-one)
    else:
        print(zero-one+1)