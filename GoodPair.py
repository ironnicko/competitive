for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    print(a.index(min(a))+1, a.index(max(a))+1)