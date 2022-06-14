from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print =lambda x : stdout.write(str(x))

for _ in range(int(input())):
    s = input()
    array = [[-1, -1] for _ in range(2)]
    ans = 0
    for i in range(len(array)):
        j =  i-1 
        p = i & 1
        if s[i] != '1': j = min(j, max(array[0][p^1], array[1][p]))
        if s[i] != '0': j = min(j, max(array[0][p], array[1][p^1]))
        ans += i-j
        if s[i] != "?": array[ord(s[i]) - ord('0')][p] = i
    print(f"{ans}"+"\n")