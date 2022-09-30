for _ in range(int(input())):
    n, k= map(int, input().split())

    a = [int(i) for i in input().split()]

    div = [0 for _ in range(k)]

    for i in range(n):
        div[(i+1)%k] = max(div[(i+1)%k], a[i])
    print(sum(div))