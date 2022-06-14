for _ in range(int(input())):
    n = int(input())
    s = input()
    f = 1
    visited = set()
    for i in range(n):
        if s[i] == 'B':
            visited.add(1)
        elif s[i] == 'R':
            visited.add(2)
        else:
            if len(visited) == 1:
                print("NO")
                f = 0
                break
            else:
                visited.clear()
    if len(visited) == 2 or len(visited) == 0 and f:
        print("YES")
    else:
        if f:
            print("NO")