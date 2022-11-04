MOD = int(1e5+1)

for _ in range(int(input())):
    n = int(input())
    n %= MOD
    arr = [int(i) for i in input()] + [0]
    flip = 0
    for i in range(n-1):
        if arr[i] - flip:
            if arr[i+1] - flip == 0:
                arr[-1] += 1
                flip = 1 - flip
    print(arr[-1])
