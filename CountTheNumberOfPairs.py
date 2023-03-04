

t = int(input())
while t:

    n, k = map(int, input().split())

    n %= int(1e9)

    s = input()

    alphabets = [0 for _ in range(100)]

    already = [0 for _ in range(30)]
    for i in s:

        alphabets[ord(i) - ord('a')] += 1

        item = i.swapcase()

        if alphabets[ord(item) - ord('a')]:

            alphabets[ord(item) - ord('a')] -= 1

            alphabets[ord(i) - ord('a')] -= 1

            already[ord(i.lower()) - ord('a')] += 1
    addd = 0
    for i in alphabets:
        addd += i//2

    final = 0
    for i in already:
        final += i
    print(final + min(addd, k))
    t -= 1
