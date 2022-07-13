for _ in range(int(input())):
    n = int(input())
    if n == 2:
        print(2)
        print(1, 2)
        continue
    arr = [1 for _ in range(n)]
    d = 2
    vis = set()
    i = 2
    index = 1
    print(2)
    while i < n:
        item = arr[index-1]*d
        if item <= n:
            arr[index] = item
            vis.add(item)
            index += 1
        else:
            if i not in vis:
                arr[index] = i
                vis.add(i)
                index += 1
            i+=1
    if n&1:
        arr[-1] = n
    print(*arr)
