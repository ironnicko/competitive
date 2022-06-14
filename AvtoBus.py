from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    n = int(input())
    f = 1
    if n<4:
        print("-1\n")
        continue
    else:
        if n&1:
            print("-1\n")
        else:
            fours = 0
            sixes=0
            count4 = 0
            count6 =0
            temp = int(n)
            while n%6!=0:
                n-=4
                count4 += 1
            sixes = n//6
            n = temp
            while n%4!=0:
                n -= 6
                count6 +=1
            fours = n//4
            fours += count6
            sixes += count4
            if fours==0 or sixes==0:
                temp = max(fours, sixes)
                print(f"{temp} {temp}\n")
            else:
                print(f"{sixes} {fours}\n")