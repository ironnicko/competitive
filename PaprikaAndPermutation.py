for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    total = 0
    p = set(range(1, n + 1))
    a_ = []
    for ai in a:
        if ai in p:
            p.remove(ai)
        else:
            a_ += [ai]
 
    for pi, ai in zip(sorted(p), a_):
        if ai == pi:
            continue
 
        if pi * 2 >= ai:
            total = -1
            break
 
        total += 1
    print(total)