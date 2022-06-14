from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print =lambda x : stdout.write(str(x))

for _ in range(int(input())):
    n = int(input())
    if n == 1 or n == 2:
        print("3\n")
    else:
        ans = n&(-n)
        if ans == n:
            ans += 1
        print(f"{ans}\n")
        