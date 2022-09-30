t = int(input())
for _ in range(t):
    N  =int(input())%1000
    N %= 10000
    if N == 4:
        print(2,1,3,4)
    else:
        arr = []
        for i in range(N):
            arr.append(i+1)
        arr[N-2] = N-1
        arr[N-3] = 1
        arr[N-4] = 3
        arr[N-5] = 2
        for i in range(N-5):
            arr[i] = i+4
        for i in arr:
            print(i, end=" ")
        print()