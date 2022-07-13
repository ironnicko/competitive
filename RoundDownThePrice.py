arr =[10**i for i in range(11)]


for _ in range(int(input())):
    n = int(input())
    for i in arr:
        if i > n and i > 0:
            print(n-(i//10))
            break