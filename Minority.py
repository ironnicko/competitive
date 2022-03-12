testCase = int(input())
while testCase > 0:
    testCase -= 1
    number = input()
    hashMap = {'1': 0, '0': 0}
    for i in number:
        hashMap[i] += 1
    ones, zeros = hashMap["1"], hashMap["0"]
    if ones > zeros:
        print(zeros)
        continue
    elif zeros > ones:
        print(ones)
        continue
    if ones == zeros:
        print(zeros - 1)
