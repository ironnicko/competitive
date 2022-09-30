for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    y = sorted([(y[i] - x[i]) for i in range(n)])
    count = 0
    ptr = n-1
    visited = set()
    for i in range(n):
        if ptr == i:
            continue
        if i not in visited and ptr not in visited:
            if (y[i] + y[ptr]) >= 0:
                count += 1
                visited.add(ptr)
                ptr -= 1
        visited.add(i)

    print(count)
