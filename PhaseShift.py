def function(pos, j):
    count = 0
    p = j
    while (p!=-1):
        count += 1
        p = pos[p]
        if p == j: 
            return count
    return -1

for _ in range(int(input())):
    n = int(input())
    n%=1000000001
    s = map(ord, input())
    letters = [1 for _ in range(26)]
    r = [-1 for _ in range(26)] # pos
    for i in s:
        if r[i - 97] == -1:
            for j in range(26):
                if letters[j] != 0 and j != i - 97:
                    r[i - 97]= j
                    tem = function(r, j)
                    if not(tem != -1 and tem != 26):
                        letters[j] = 0
                        break
    
        ans = i - 97
        ans = r[ans]
        ans += 97
        print(chr(ans), end="")
    print()
