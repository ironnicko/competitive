from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print =lambda x : stdout.write(str(x))

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    odds = 0
    min_c = float('inf')
    for i in a:
        if i&1: odds += 1
    if odds:
        print(f"{n-odds}\n")
    else:
        for i in a:
            local = 0
            while not(i&1):
                i //= 2
                local += 1
            min_c = min(min_c, local)
        print(f"{min_c + n-odds-1}\n")