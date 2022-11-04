from collections import defaultdict
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    num_list = defaultdict(list)
    color_list = [0 for _ in range(n)]
    for i in range(n):
        num_list[a[i]].append(i)
    sum = 0
    for i in num_list:
        sum += min(len(num_list[i]), k)
    sum -= sum % k
    color = 0
    for i in num_list:
        for j in range(min(k, len(num_list[i]), sum)):
            color_list[num_list[i][j]] = color + 1
            sum -= 1
            color = (color + 1) % k
    print(*color_list)