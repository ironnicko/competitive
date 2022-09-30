for _ in range(int(input())):
    n = int(input())
    pos = [int(i) for i in input().split()]
    times  = list(map(int, input().split()))
    left = []

    right = []

    for i in range(n):
        left.append(pos[i] + times[i])
        right.append(left[i] - (2 * pos[i]))
    print((max(left) - max(right))/2)