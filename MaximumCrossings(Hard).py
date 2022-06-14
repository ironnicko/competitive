from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print = stdout.write

def Mod_FenwickTree(i):
    """
        So a fenwick tree is being used to calculate the running sum for every value that is being put in,
        but the kicker or the twist here is that while updating we increase the values by only one.
    """
    res = 0
    j = i

    while i > 0: # add
        res += bit[i]
        i -= i&-i

    while j <= n: # update
        bit[j] += 1
        j += j&-j

    return res
 
for _ in range(int(input())):
    n = int(input())
    
    s, bit = 0, [0]*(n+1)
    for x in input().split()[::-1]:

        s += Mod_FenwickTree(int(x))

    print(f"{s}\n")