from sys import stdin, stdout

input = stdin.readline
def print(*args):
    for i in args:
        stdout.write(str(i) + " ")


for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    A_Copy = A[::]

    A.sort()

    sum1, max1 = 0, 0

    for i in range(n):
        if sum1 < A[i]:
            max1 = A[i]
        sum1 += A[i]

    ans1 = []

    for i in range(n):
        if A_Copy[i] >= max1:
            ans1.append(i + 1)

    print(len(ans1))
    stdout.write("\n")
    print(*ans1)
