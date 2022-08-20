for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    final = ["B" for _ in range(m)]
    vis = set()

    for i in a:
        selected = min(m+1-i, i)
        if i == selected and selected-1 in vis:
            selected = m+1-i
        elif selected == m+1-i and selected-1 in vis:
            selected = i
        selected -= 1
        vis.add(selected)
        final[selected] = "A"
    print("".join(final))