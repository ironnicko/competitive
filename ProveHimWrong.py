from math import pow
for _ in range(int(input())):
    n = int(input())
    if n > 19:
        print("NO")
    else:
        print("YES")
        for  i in range(n):
            if i == n-1:
                print(pow(3, i))
            else:
                print(pow(3, i), end=" ", sep=" ")
