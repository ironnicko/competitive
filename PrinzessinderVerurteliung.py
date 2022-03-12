from string import ascii_lowercase

for _ in range(int(input())):
    length = int(input())
    strg = input()
    flag = False

    for i in ascii_lowercase:
        if flag: break
        if i not in strg:
            print(i)
            flag = True
            break

    if flag: continue
    for i in ascii_lowercase:
        if flag: break
        for j in ascii_lowercase:
            if i+j not in strg and not flag:
                print(i+j)
                flag = True
                break

    if flag: continue
    for i in ascii_lowercase:
        if flag: break
        for j in ascii_lowercase:
            if flag: break
            for k in ascii_lowercase:
                if i+j+k not in strg and not flag:
                    print(i+j+k)
                    flag = True
                    break