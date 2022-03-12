n = int(input())
A = sorted([int(i) for i in input().split()])

left, right = [], []
middle = max(A)
for i in A:
    if i not in right and middle != i:
        right.insert(0, i)
    elif i not in left and middle != i:
        left.append(i)
print(len(left) + len(right) + 1)
if left:
    print(*left, end=" ")
print(middle, end=" ")
if right:
    print(*right)