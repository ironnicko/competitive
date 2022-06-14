from sys import stdin,stdout
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    s = input().rstrip()
    n = len(s)
    f =1
    visited = {}
    characters = set(s)
    if len(characters) == 1:
        print("YES\n")
        continue
    for i in range(n):
        if not f:
            break
        if s[i] in visited:
            if i - visited[s[i]] <= len(characters)-1:
                print("NO\n")
                f = 0
                break
        visited[s[i]] = i
        
    if f:
        print("YES\n")