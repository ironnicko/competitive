for _ in range(int(input())):
    n = int(input()) % int(1e6+1)
    items = []
    minimize = float("inf")
    for i in map(int, input().split()):
        items.append(i)
        minimize = min(i, minimize)
    print(("Alice", "Bob")[minimize == items[0]])
