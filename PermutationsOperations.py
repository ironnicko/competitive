MOD = 1000001
for _ in range(int(input())):
    size_n = int(input()) % MOD
    main = [int(i) % MOD for i in input().split()]
    prefix = []
    local_maxima = main[0]
    for i in range(size_n):
        local_maxima = max(main[i], local_maxima)
        prefix.append(local_maxima)
    ranges = []
    for i in range(size_n):
        ranges.append(0)
    for i in range(size_n):
        if main[i] < prefix[i]:
            ranges[i] = i

    def comparator(i): return prefix[i] - main[i]
    ranges = sorted(ranges, key=comparator)

    p = [print(i+1, end=" ") for i in ranges]
    print("\n", end="")
