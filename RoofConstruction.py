def swap(number):
    if number == 2:
        print("0 1")
        return
    swapable = list(range(number))
    limit = len(bin(swapable[-1])[2:])
    set = {i: [] for i in range(1, limit+1)}
    for number in swapable:
        key = len(bin(number)[2:])
        set[key].append(number)
    result = list(set.values())
    change = result.pop(-1)[::-1]
    result.insert(0, change)
    empty = []
    [empty.extend(i) for i in result]
    print(*empty[::-1])

testCase = int(input())
while testCase > 0:
    testCase -= 1
    swap(int(input()))