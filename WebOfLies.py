from sys import stdin,stdout
input = lambda: stdin.buffer.readline().strip().decode()
print = stdout.write
n, m = map(int, input().split())
d = [0] * (n + 1)
a = n
for _ in range(m):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    d[u] += 1
    if d[u] == 1:
        a -= 1
for _ in range(int(input())):
    s = input()
    if s[0] == '1':
        _, u, v = map(int, s.split())
        if u > v:
            u, v = v, u
        d[u] += 1
        if d[u] == 1:
            a -= 1
    elif s[0] == '2':
        _, u, v = map(int, s.split())
        if u > v:
            u, v = v, u
        d[u] -= 1
        if d[u] == 0:
            a += 1
    else:
        print(f"{a}\n")
