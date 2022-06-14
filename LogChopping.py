for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    print(('maomao90', 'errorgorn')[(sum(a) - n)%2])