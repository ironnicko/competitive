for _ in range(int(input())):
    a, b  = map(int, input().split())
    sum = a + (b*2)
    if not a:
        print(1)
    else:
        print(sum+1)