from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    arr = sorted(map(int, input().split()))
    if any(arr.count(i) > 1 for i in arr):
        print("NO")
    else:
        ans = "YES"
        p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
        for i in p:
            count = [0 for i in range(i)]
            for elem in arr:
                count[elem % i] += 1
            if min(count) >= 2:
                ans = "NO"
        print(ans)
