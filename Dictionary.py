from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    s = input().rstrip()
    ans = 1
    f =1 
    for i in range(26):
        if not f:
            break
        for j in range(26):
            if ord('a') + i == ord(s[0]) and ord('a') + j == ord(s[1]):
                f =0 
                break
            elif ord('a') + i != ord('b') + j:
                ans += 1
    print(str(ans - 1)+"\n")