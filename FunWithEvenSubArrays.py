testCase = int(input())
while testCase > 0:
    testCase -= 1
    length = int(input())
    array = [int(i) for i in input().split()]
    count = 0
    counter = 1
    i = len(array) - 2
    while i >= 0:
        if array[i] == array[-1]:
            i -= 1
            counter += 1
        else:
            i -= counter
            count += 1
            counter *= 2
    print(count)