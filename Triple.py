for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    dic = {
        1 : 0,
        0 : 0
        }
    for i in a:
        dic[i%2] += 1
    par = a[0]%2
    f = 1
    for i in a[1:]:
        if par != i%2:
            par = i%2
        else:
            if dic[i%2] == n:
                print("YES")
            else:
                print("NO")
            f = 0
            break
    if f:
        print("YES")

# from collections import Counter
# for _ in range(int(input())):
#     n = int(input())
#     array = [int(i) for i in input().split()]
#     array = Counter(array)
#     flag = 1
#     for item in array:
#         if array[item] > 2:
#             print(item)
#             flag = 0
#             break
#     else:
#         if flag:
#             print(-1)