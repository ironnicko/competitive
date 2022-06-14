from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    s = input().rstrip()
    t = input().rstrip()
    f = 1
    for i in range(len(t)):
        if not f:
            break
        if t[i] == 'a':
            if len(t) > 1:
                print('-1\n')
            else:
                print('1\n')
            f = 0
    if f:
        print(f"{2**len(s)}\n")