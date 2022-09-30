for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        for j in range(i+1):
            print(int(j == 0 or j==i), end=" ")
        print()