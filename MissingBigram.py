def MissingBigrams(letters=["ab", "bb", "ba", "aa", "ba"]):
    letter = 1
    final = letters[0]
    ok = 1
    while letter != len(letters):
        if letters[letter][0] == letters[letter-1][1]:
            final += letters[letter][1]
        else:
            final += letters[letter]
            ok = 0
        letter += 1
    if ok: final+="a"
    print(final)
    
test_cases = int(input())
while test_cases > 0:
    test_cases -= 1
    length = int(input())
    letters = input().split()
    MissingBigrams(letters)