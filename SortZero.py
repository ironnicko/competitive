for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(0)
    else:
        score = 0
        a = [int(i) for i in input().split()][::-1]
        i = 1
        while i < n:
            if a[i] > a[i-1]:
                break
            i+=1
        S = set(a[i:])
        i = 0
        while i < n:
            if a[i] in S:
                break
            i+=1
        print(len(set(a[i:])))