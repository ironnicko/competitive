testCase = int(input())
while testCase > 0:
    testCase -= 1
    number = int(input())
    mod = number % 7
    lastDigit = number%10
    if mod == 0:
        print(number)
        continue
    
    if lastDigit + (7 - mod) > 9:
        print(number - mod)
    else:
        print(number + (7 - mod))