def greater_than_most(strings, letter):
    arr = []

    for i in range(n):
        arr.append(2 * strings[i].count(letter) - len(strings[i]))

    arr.sort(reverse=1)

    last = 0
    count = 0

    for i in arr:
        if last + i > 0:
            last += i 
            count += 1
            continue
        break
    return count

for _ in range(int(input())):
    n = int(input())

    strings = [input() for _ in range(n)]

    ans = 0
    for i in "abcde":
        ans = max(ans, greater_than_most(strings, i))
    print(ans)
