for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    if a[0] < a[-1]:
        print("YES")
    else:
        print("NO")