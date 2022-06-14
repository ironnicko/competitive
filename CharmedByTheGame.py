for _ in range(int(input())):
    a, b = map(int, input().split())
    diff = abs(a-b)//2
    sum = a +b 
    if sum % 2 == 0:
        array = [i for i in range(diff, sum-diff+1, 2)]
        print(len(array))
        print(*array)
    else:
        array = [i for i in range(diff, sum-diff+1)]
        print(len(array))
        print(*array)