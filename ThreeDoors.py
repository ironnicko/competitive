
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    try:
        if a[a[a[n - 1] - 1] - 1] == 0:
            print("YES")
        else:
            print("NO")
    except:
        print("NO")