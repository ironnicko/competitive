from string import ascii_lowercase
from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print =lambda x : stdout.write(str(x))

for _ in range(int(input())):
    n = int(input())
    n = (n*2)+1
    count = {i:0 for i in ascii_lowercase}

    # we are only getting the first alphabet that is of odd length
    # this is because the first character occurance will be as follows:
    # 1 + x + y + z + z + x - y [for a 4 long string]
    # when we use association property it becomes:
    # 1 + 2(x + z) 
    # therefore we can conclude that the first letter will be of odd decent and other letters will be of even decent.

    for i in range(n):
        for j in input():
            count[j] += 1

    for i in sorted(count):
        if count[i]&1:
            print(i+"\n")
            break