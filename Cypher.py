for _ in range(int(input())):
    given_N = int(input())
    array = [int(i) for i in input().split()]
    I = 0


    MOD = 100000000


    while I < given_N:

        m, order = input().split()

        for i in order:
            if i == 'D':
                if array[I%MOD] < 9: 
                    array[I%MOD] += 1
                else:
                    array[I%MOD] = 0
            else:
                if array[I%MOD] > 0:
                    array[I%MOD] -= 1
                else:
                    array[I%MOD] = 9
                
        I += 1
    for i in array:
        print(i, end=" ")
    print()