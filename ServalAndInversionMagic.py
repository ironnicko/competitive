for _ in range(int(input())):
    n = int(input())
    s = input()

    i = n//2
    j = (n+1)//2

    if i == j:
        j += 1
    if n & 1:
        i -= 1
    else:
        i -= 1
        j -= 1

    one, two = s[:i+1], s[j:][::-1]

    prev = -1
    ans = "Yes"
    for i in range(len(one)):
        if one[i] != two[i]:
            if prev == i-1 or prev == -1:
                prev = i
            else:
                ans = "No"
    print(ans)
