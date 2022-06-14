from collections import Counter
from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n, g = map(int, input().split())
    arr = list(map(int, input().split()))
    db = dict()
    
    for i in range(n):
        if arr[i] in db:
            db[arr[i]] += 1
        else:
            db[arr[i]] = 1
    
    db = list(db.items())
    keys = []
    
    for i in range(len(db)):
        if db[i][1] >= g:
            keys.append(db[i][0])
    keys.sort()
    n = len(keys)
    if n == 0:
        print("-1\n")
        continue
    ans_l = keys[0]
    ans_r = keys[0]
    ans_length = 0
    
    l = keys[0]
    r = keys[0]
    
    for i in range(1, len(keys)):
        if keys[i] == keys[i - 1] + 1:
            r = keys[i]
            if r - l > ans_r - ans_l:
                ans_l = l
                ans_r = r
                ans_length = r - l
        else:
            l = keys[i]
            r = keys[i]
    
    if r - l > ans_r - ans_l:
        ans_l = l
        ans_r = r
        ans_length = r - l
    print(f"{ans_l} {ans_r}\n")
