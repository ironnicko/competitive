testCase = int(input())
while testCase>0:
    testCase -= 1
    length, no_of_operations =  input().split()
    length, no_of_operations = int(length), int(no_of_operations)
    letters =  input()

    if letters[::-1] == letters or no_of_operations == 0:
        print(1)
    elif no_of_operations > 1:
        if length%2 == 0 and letters[:(length//2)] == letters[(length//2):] :
            print(1)
        elif length%2 == 1 and letters[:(length//2)] == letters[(length//2) + 1: ]:
            print(1)
        else:
            print(2)
    else:
        print(2)