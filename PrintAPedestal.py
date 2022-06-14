from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print =lambda x : stdout.write(str(x))

for _ in range(int(input())):
    n = int(input())
    n_cp = int(n)
    n //= 3
    main = [n+1, n, n-1]
    condition = sum(main) < n_cp*3
    diff = n_cp - sum(main) if condition else sum(main) - n_cp
    i=0
    while diff:
        main[i%3] += 1
        i = i + 1
        diff -= 1
    print(f"{main[1]} {main[0]} {main[2]}\n")