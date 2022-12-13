for _ in range(int(input())):
    s = input()
    n = len(s) 
    dis = "Yes"
    if s[0] not in dis:
        print("NO")
        continue
    else:
        index = dis.index(s[0])
        for i in range(n):
            if s[i] != dis[index]:
                dis = "NO"
                break
            index += 1
            index %= 3
    print(dis.upper())
