from bisect import bisect_left, bisect_right
n = int(input())

arr = list(map(int, input().split()))

brr = list(map(int, input().split()))

total = n*(n-1)//2

crr = sorted(zip(arr, brr), key=lambda x: x[0] - x[1])
differences = [x[0] - x[1] for x in crr]
# print(crr, differences, sep="\n")

final = 0

for x, i in enumerate(differences):
    final += n  - bisect_left(differences, -i + 1, x+1)
print(final)