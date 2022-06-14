from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    a = sorted([int(i) for i in input().rstrip().split()])
    main = [0 for _ in range(n)]
    f=0
    constant =0
    for i in range(0, n, 2):
        main[i]=a[constant]
        constant+=1
    for i in range(1, n, 2):
        main[i] = a[constant]
        constant+=1

    for i in range(1, n-1):
        if not((main[i] > main[i -1] and main[i] > main[i +1]) or (main[i] < main[i + 1] and main[i] < main[i - 1])):
            f = 1
    if (not(main[0] < main[n - 1] and main[0] < main[1] and main[n - 1] > main[n - 2])):
        f = 1
    if f:
        print("NO\n")
    else:
        print("YES\n")
        for i in main:
            print(f"{i} ")
        print("\n")