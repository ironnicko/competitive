for _ in range(int(input())):
    k = int(input().split()[1])
    cost = [float('inf')] + [1] * 26
    for x in input():
        x = ord(x) - ord("a")
        while k >= cost[x]:
            k -= cost[x]
            cost[x] = 0
            x -= 1
        print(chr(ord("a") + x), end="")
    print()
