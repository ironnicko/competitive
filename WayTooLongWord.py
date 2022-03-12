def main(string):
    if len(string) > 10:
        string = list(string)
        first, last = string.pop(0), string.pop(-1)
        print(first + str(len(string)) + last)
    else:
        print(string)

test_cases = int(input())
while test_cases > 0:
    main(input())
    test_cases -= 1