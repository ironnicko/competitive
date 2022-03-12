for _ in range(int(input())):
    n, a, b = map(int, input().split())
    numbers = list(range(1, n+1))
    if abs(a - b) > 1 or a + b > n -2:
        print(-1)
        continue
    if a == b:
        i = 1
    elif a > b:
        i = 0
        numbers = numbers[::-1]
    elif b > a:
        i = 0
    integer = max(a, b)
    for __ in range(integer):
        numbers.insert(i, numbers.pop(-1))
        i += 2
    print(*numbers)