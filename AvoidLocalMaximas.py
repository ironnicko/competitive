"""
    If the no of maxima's is odd, then we print maxima's - 1 since the answer will be the number of minima's;
    If the no of maxima's is even, then we print maxima's//2;
    If maxima == 1, then we print one back since there will be only one area to fix.
"""
for _ in range(int(input())):
    length = int(input())
    array = [int(i) for i in input().split()]
    count = 0
    maximas = 0

    for i in range(1, length-1):
        if array[i-1] < array[i] > array[i+1]:
            array[i+1] = max(array[i], array[i+2] if i+2 < length else 0)
            count += 1
    print(count)
    print(*array)