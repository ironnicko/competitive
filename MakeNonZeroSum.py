MOD = int(2e6)

for _ in range(int(input())):
    n = int(input())
    n %= MOD
    array = list(map(int, input().split()))
    if n & 1:
        print(-1)
    else:
        counter = 0
        for i in range(0, n-1,2 ):
            counter += 1 + int(array[i] * array[i+1] == -1)
        print(counter)
        for i in range(0, n-1, 2):
            if(array[i] * array[i+1] == -1):
                print(f"{i+1} {i+1}")
                print(f"{i+2} {i+2}")
            else:
                print(f"{i+1} {i+2}")