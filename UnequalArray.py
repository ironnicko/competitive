for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    first, second =0, 0
    flag = 0
    for i in range(n-1):
        if a[i] == a[i+1]:
            first = i+1
            flag = 1
            break
    for i in range(n-1, 0, -1):
        if a[i] == a[i-1]:
                second = i-1
                flag = 1
                break
    if flag:
        if second < first:
            print(0)
        elif first == second :
            print(1)
        else:
            print(second - first)
    else:
        print(0)
