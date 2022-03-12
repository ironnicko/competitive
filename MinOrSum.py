for _ in range(int(input())):
    length = int(input())
    array = [int(i) for i in input().split()]
    last = 0
    for i in array:
        last |= i
    print(last)