from collections import defaultdict

t = int(input())
for _ in range(t):
    n, COST = map(int, input().split())
    n %= 200
    COST %= 200

    planets = list(map(int, input().split()))


    orbits = defaultdict(int)

    final_Cost = 0 

    for i in planets:
        orbits[i] += 1

    for i in orbits:
        final_Cost += min(COST, orbits[i])

    print(final_Cost)