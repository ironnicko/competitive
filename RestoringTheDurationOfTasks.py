from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print =lambda x : stdout.write(str(x))

MOD = 1e4

for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    bar = [int(i) for i in input().split()]
    prev = -1
    print(f"{bar[0] - arr[0]} ")
    for i in range(1, n):


        if bar[i-1] > arr[i]:
            prev = bar[i-1] - arr[i]
        else:
            prev = 0

        final = bar[i]-prev - arr[i]
        print(f"{final} ")
        prev = bar[i]

        
    print("\n")