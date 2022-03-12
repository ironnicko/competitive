def SquareString(letters):
    if len(letters)%2 == 0:
        if letters[ :(len(letters)//2)] == letters[ (len(letters)//2)  : ]:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

test_cases = int(input())
while test_cases > 0:
    test_cases -= 1
    letters = input()
    print(SquareString(letters))