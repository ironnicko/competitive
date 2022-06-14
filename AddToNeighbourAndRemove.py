"""
            Sum of array
    Value = ------------------------
            Number of elements - K

            Here 'K' denotes number of operations required
            to get all the elements equal to each other.
"""
def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    s = sum(a)
    for i in range(n, 0, -1):
        needSum = s/i
        currSum = 0
        f =  1
        # the iteration here is to find the 'K'
        for j in range(n):
            currSum += a[j]
            if currSum > needSum:
                f = 0
                break
            elif currSum == needSum:
                currSum = 0
        if f:
            print(n-i)
            return
for _ in range(int(input())):
    solve()