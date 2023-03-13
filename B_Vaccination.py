# N is the number of people
# K is the number of vaccines present in the pack
# D is the number of seconds a vaccine can be taken out of fridge
# W is the number of seconds a patient can wait from their arrival

for _ in range(int(input())):
    n, k, d, w = map(int, input().split())
    pat = list(map(int, input().split()))

    curr = 0
    vac = -1
    placed = -1
    for i in range(n-1, -1, -1):
        if placed == -1 or vac == 0:
            placed = max(0, pat[i] - d)
            vac = int(k)
            curr += 1
        if pat[i] + w >= placed:
            vac -= 1
        else:
            placed = max(0, pat[i] - d)
            vac = int(k) - 1
            curr += 1


    print(curr)