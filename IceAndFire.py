
for _ in range(int(input())):
    n = int(input())
    s = input()
    val = s[0]
    prev = 1
    current = 1
    for i in s:
        current += 1
        if val != i:
            prev = current - 1
        val = i
        print(prev, end=" ")
    print()