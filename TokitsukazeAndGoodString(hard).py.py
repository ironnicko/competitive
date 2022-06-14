from sys import stdin, stdout

input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    s = input().rstrip()
    ans = 0
    ans2 = 0
    r = float('-inf')
    for i in range(0,n,2):
        a = s[i]
        b = s[i+1]
        if a != b:
            ans += 1
        else:
            if a != r:
                r = a
                ans2 += 1

    print(str(ans)+" "+str(max(ans2, 1))+"\n")