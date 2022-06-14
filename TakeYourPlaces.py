for _ in range(int(input())):
    n = int(input())
    even, odd, even_elems, odd_elems = 0, 0, 0, 0
    arr = [int(i) for i in input().split()]
    for i in range(n):
        if arr[i] % 2:
            odd += 1
            odd_elems += abs(even - odd)
        else:
            even += 1
            even_elems += abs(even - odd)
    if abs(even - odd) > 1:
        print(-1)
    else:
        if even > odd:
            print(odd_elems)
        elif odd > even:
            print(even_elems)
        else:
            print(min(odd_elems, even_elems))