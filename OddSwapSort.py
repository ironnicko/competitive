for _ in range(int(input())):
    n=int(input())
    arr=[int(i) for i in input().split()]
    dupe=[0,0]
    if arr==sorted(arr):print('Yes')
    else:
        for i in arr:
            if i%2==1:
                if i>=dupe[1]:dupe[1]=i
                else:
                    print('No')
                    break
            else:
                if i>=dupe[0]:dupe[0]=i
                else:
                    print('No')
                    break
        else:print('Yes')