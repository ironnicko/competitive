for _ in range(int(input())):
    n = int(input())
    A = [int(i) for i in input().split()]

    ones, zeroes = A.count(1), A.count(0)
    if ones > zeroes:
        final = "1" * ones
        if len(final)%2:
            ones -= 1
            final = "1" * ones
        print(ones)
    else:
        final = "0" * zeroes
        print(zeroes)
    print(" ".join(final))