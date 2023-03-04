s = "meow"

for _ in range(int(input())):
    n = int(input())
    s = input().lower()

    se = set()

    res = ""

    for i in range(n-1):
        if s[i] != s[i+1]:
            res += s[i]
    res += s[n-1]
    if res == 'meow':
        print("YES")
    else:
        print("NO")

