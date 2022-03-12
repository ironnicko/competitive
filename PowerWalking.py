for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    length = len(set(a))
    some = n - length
    for i in range(n, some, -1):
        print(length, end=" ")
    length += 1
    for j in range(some):
        print(length+j, end=" ")
    print()