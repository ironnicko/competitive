for _ in range(int(input())):
    n = int(input())
    a = input()
    solved = 0

    for i in range(n):
        if a[i] == '0':
            solved = 1
            if i >= n//2:
                print(1, i+1, 1 ,i)
                break
            else:
                print(i+2, n, i+1, n)
                break
    if not solved:
        print(1, n-1, 2, n)