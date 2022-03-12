testCase = int(input())
while testCase > 0:
    testCase -= 1
    length = int(input()) - 1
    a = [int(i) for i in input().split()]
    if a != sorted(a):
        for i in range(length):
            if a[i] != i+1:
                target = a.index(i+1)
                target_slice = a[i: target+1]
                break
        
        del a[i: target+1]
        for item in target_slice:
            a.insert(i, item)
    print(*a)