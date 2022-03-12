testCase = int(input())
while testCase > 0:
    testCase -= 1
    length = int(input())
    string = input()
    string = list(string)
    zeroes, ones = string.count("0"), string.count("1")
    if ones>0 and zeroes==1:
        print("BOB")
        continue
    if ones == length:
        print("DRAW")
        continue
    if zeroes % 2 == 0 and length > 1:
        print("BOB")
    elif zeroes % 2 == 1 and length > 1:
        print("ALICE")
    elif length == 1:
        print("BOB") if string[0] == "0" else print("ALICE")