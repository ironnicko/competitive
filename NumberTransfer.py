from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    x, y = map(int, input().rstrip().split())
    if x > y:
        print("0 0"+'\n')
    else:
        if not(y%x):
            ans = y//x
            print(f"1 {ans}"+"\n")
        else:
            print("0 0"+'\n')