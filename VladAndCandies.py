for _ in range(int(input())):
    n = int(input())
    arr = sorted([int(i) for i in input().split()])
    val = arr.pop()
    if not arr and val == 1:
        print("YES")
    elif not arr and val > 1:
        print("NO")    
    else:
        sec = arr[-1]
        if val -1 == sec or val == sec:
            print("YES")
        else:
            print("NO")