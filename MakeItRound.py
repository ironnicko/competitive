
for _ in range(int(input())):
    n,m = map(int, input().split())
    n_c = int(n)
    tot = 1

    # Take out all the 10's from N

    while n%10 == 0 : n//=10

    # Take out all five's and replace them with 2
    
    while n%5==0 and tot*2<=m:
        tot*=2
        n//=5    

    # Take out all two's and replace them with 5

    while n%2==0 and tot*5<=m:
        tot*=5
        n//=2   

    # Add in 10's while the total is less than M

    while tot*10<=m:tot*=10

    print(n_c * tot * (m//tot))