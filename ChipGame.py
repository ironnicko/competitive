t = int(input())
for _ in range(t):
    n, m = [int(i) for i in input().split()]
    if m & 1 != n & 1:
        print("Burenka")
    else:
        print("Tonya")