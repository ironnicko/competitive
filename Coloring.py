for _ in range(int(input())):
    n, _, k = map(int, input().split())

    print(("YES", "NO")[max(list(map(int, input().split()))) > (n + k - 1) // k])