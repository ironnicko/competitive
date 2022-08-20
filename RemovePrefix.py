for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    SET = set()
    score  =0
    for i in reversed(range(n)):
        if a[i] in SET:
            break
        else:
            score +=1
        SET.add(a[i])

    print(n-score)