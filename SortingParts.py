testCase = int(input())
while testCase>0:
    testCase -= 1
    n = int(input())
    a = [int(i) for i in input().split()]

    print("NO") if a == sorted(a) else print('YES')