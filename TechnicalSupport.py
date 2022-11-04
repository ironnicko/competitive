for _ in range(int(input())):
    n = int(input())
    s = input()

    stk = []

    for i in s:
        if i == "Q":
            stk.append('Q')
        else:
            if stk:
                stk.pop()
    print(("No", "Yes")[stk == []])
