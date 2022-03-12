for i in range(int(input())):
    string = input()
    main = "rgb"
    for i in main:
        if string.index(i) > string.index(i.upper()):
            print("NO")
            break
    else:
        print("YES")