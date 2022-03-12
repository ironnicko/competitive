for _ in range(int(input())):
    A = [int(i) for i in input().split()] 
    B = [int(i) for i in input().split()] 
    C = [int(i) for i in input().split()] 

    distance = 0

    if A[1] == B[1] and A[1] == 0:
        print(0)
        continue
    elif B[1] == C[1] and C[1] == 0:
        print(0)
        continue
    elif A[1] == C[1] and A[1] == 0:
        print(0)
        continue

    if A[1] == B[1] and B[1] > C[1]:
        print(abs(A[0] - B[0]))
        continue
    elif B[1] == C[1] and B[1] > A[1]:
        print(abs(B[0] - C[0]))
        continue
    elif A[1] == C[1] and A[1] > B[1]:
        print(abs(A[0] - C[0]))
        continue
    else:
        print(0)
        continue