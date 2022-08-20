for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    sum = 0
    z = 0
    for i in a:
        sum +=  i
        z += int(sum and i == 0)

    ans = sum + z - a[-1] - int(a[-1] == 0)
    print(max(0, ans))
