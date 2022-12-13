for _ in range(int(input())):
    number = int(input()) % 1000
    if number == 1:
        print(1, "\n1", 2)
        continue
    number = 3 * number
    left1, right, kite = 1, number, 0
    while left1 < right:
        kite += 1
        left1 += 3
        right -= 3
    left1 = 1
    right = number
    print(kite)
    while left1 < right:
        print(left1, right)
        left1 += 3
        right -= 3
