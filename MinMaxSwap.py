def MinMaxSwap(size, a=None, b=None):
    temp = 0
    while temp < size:
        if a[temp] > b[temp]:
            a[temp], b[temp] = b[temp], a[temp]

        temp += 1

    a, b  = sorted(a), sorted(b)

    print(a[-1] * b[-1])

test_no = int(input())
while test_no > 0:
    size = int(input())
    array_1 = [int(i) for i in input().split()]
    array_2 = [int(i) for i in input().split()]
    MinMaxSwap(size ,array_1, array_2)
    test_no -= 1
