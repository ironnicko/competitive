
n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
inp = list(map(int, input().split()))

dict = {i:i for i in inp}

for i in range(n):
    for j in range(n-i):
        arr[i+j][j] = inp[j]
    inp.remove(i+1)
for i in arr:
    print(*(c for c in i if c))

# Greedily make L shapes and that should do it.