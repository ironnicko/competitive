testCase = int(input())
while testCase > 0:
    testCase -= 1
    length = int(input())
    sum = 1
    array = [int(x) - i for i, x in enumerate(input().split())]
    hash = {}
    for i in array:
        if i not in hash:
            hash[i] = 0
            sum = 1
        else:
            hash[i] += 1 * sum
            sum += 1
    sum = 0
    for i in hash.values():
        sum += i
    print(sum)