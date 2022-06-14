from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    s = input().rstrip()
    checker = [0, 0, 0]
    indices =[-1, -1, -1]
    ans = float('inf')
    for i in range(len(s)):
        checker[int(s[i])-1] = 1
        indices[int(s[i])-1] = i
        if all(checker):
            copy = sorted(indices)
            final = copy[0] - copy[-1] + copy[1] - copy[-1]
            ans = min(ans, abs(final))
    print(str((ans if ans != float('inf') else 0))+"\n")