for _ in range(int(input())):
    n = int(input())
    arr = sorted(map(int, input().split()))

    final = 1 + int(0 != arr[0])
    for i in range(1, n): 
        final += int(arr[i-1] < i and arr[i] >= i+1)
    print(final)
