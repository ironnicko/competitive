from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n,k = map(int,input().rstrip().split())
    c = [0]*27
    for i in input().rstrip(): c[ord(i)-ord('a')] += 1
    for i in input().rstrip(): c[ord(i)-ord('a')] -= 1
    a = 0
    for i in c:
        if i:
            if abs(i)%k==0 and a >= 0:
                a += i
            else:
                print('no\n')
                break
    else: print('yes\n')