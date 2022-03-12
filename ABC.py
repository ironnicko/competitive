testCase = int(input())
while testCase>0:
    testCase -= 1
    leng = int(input())
    to_compare = {0:0, 1:0}
    string = input()
    if leng > 2:
        print("NO")
    else:
        if leng == 2:
            if string[0] == string[1]:
                print("NO")
            else:
                print("YES")
        else:
            print("YES")
