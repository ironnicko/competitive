n = int(input())
a = [int(i) for i in input().split()]

for i in a:
    count = 0
    for j in range(1, i+1):
        if count > 3:
            continue
        if not(i%j):
            count += 1
    print("YES") if count == 3 else print("NO")