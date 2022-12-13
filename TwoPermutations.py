for _ in range(int(input())):

    n, a, b = map(int, input().split())
    if n == a == b:
        print("Yes")
    else:
        print(("No", "Yes")[((n - (a+b)) >= 2) or (n == a and n == b)])
