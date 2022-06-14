for _ in range(int(input())):
    n, k = map(int, input().split())
    A = sorted([int(i) for i in input().split()])
    limit = n
    for i in range(n):
        if A[i] >=0:
            limit = i
            break
    pos = A[limit:][::-1]
    neg = [abs(i) for i in A[:limit]]
    count = 0
    for i in range(0, len(neg), k):
        count += neg[i]
    for i in range(0, len(pos), k):
        count += pos[i]
    count *= 2
    if not neg:
        count -= pos[0]
    elif not pos:
        count -= neg[0]
    else:
        count -= max(pos[0], neg[0])
    print(count)