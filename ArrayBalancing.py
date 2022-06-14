for _ in range(int(input())):
    List = list
    n = int(input())
    a : List = [int(i) for i in input().split()]
    b : List = [int(i) for i in input().split()]
    sum : int = 0
    for i in range(n):
        if a[i] < b[i]:
            b[i], a[i] = a[i], b[i]
        if i > 0:
            sum += abs(a[i] - a[i-1]) + abs(b[i] - b[i-1])
    print(sum)