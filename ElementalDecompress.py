from bisect import bisect_left, bisect_right
from collections import Counter
for _ in range(int(input())):
    n = int(input())

    arr = list(map(int, input().split()))
    ind = {i: x for x, i in enumerate(arr)}
    count = Counter(arr)
    if n == 1:
        print("YES", 1, 1, sep="\n")
    elif any((i > 2 or i == n) for i in count.values()):
        print("NO")
    else:
        idx1 = ["nope" for _ in range(n+1)]
        idx2 = list(idx1)

        first = [0 for _ in range(n)]
        second = list(first)
        f = 0
        vis1 = set()
        vis2 = set()

        for i in range(n):
            if idx1[arr[i]] == 'nope':
                idx1[arr[i]] = i
                first[i] = arr[i]
            elif idx2[arr[i]] == 'nope':
                idx2[arr[i]] = i
                second[i] = arr[i]
            else:
                f = 1
        if f:
            print("NO")
        else:
            for i in range(1, n+1):
                if idx1[i] == 'nope':
                    vis1.add(i)
                if idx2[i] == 'nope':
                    vis2.add(i)
            start1 = 0
            start2 = 0
            item1 = list(vis1)
            item2 = list(vis2)
            for i in range(n):
                if first[i] == 0:
                    idx = bisect_right(item1, first[i], start1)
                    if idx == -1:
                        f = 1
                        break
                    else:
                        idx -= 1
                        first[i] = idx
                        if idx in vis1:
                            vis1.remove(idx)
                        start1 = idx + 1
                else:
                    idx = bisect_right(item2, second[i], start2)
                    if idx == -1:
                        f = 1
                        break
                    else:
                        idx -= 1
                        second[i] = idx
                        if idx in vis2:
                            vis2.remove(idx)
                        start2 = idx + 1
                item1 = list(vis1)
                item2 = list(vis2)

            for i, x in enumerate(arr):
                if first[i] == -1:
                    idx = bisect_left(item1, x-1)
                    first[i] = item1[idx - int(idx == len(item1))]

            for i, x in enumerate(arr):
                if second[i] == -1:
                    idx = bisect_left(item2, x-1)
                    second[i] = item2[idx - int(idx == len(item2))]

            if f:
                print("NO")
            else:
                print("YES")
                print(*first)
                print(*second)
