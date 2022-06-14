from sys import stdin, stdout

input = stdin.readline
print = stdout.write

ans = []
for _ in range(int(input())):
    n, m = map(int, input().rstrip().split())
    a = [[int(i) for i in input().rstrip().split()] for _ in range(n)]
    the_ones = set()
    for row in a:
        sorted_row = sorted(row)
        for i in range(m):
            if sorted_row[i] != row[i]: the_ones.add(i)
    if len(the_ones) == 0:
        ans.append("1 1")
    elif len(the_ones) == 2:
        c1, c2 = sorted(the_ones)
        for row in a:
            if row[c1] < row[c2]:
                ans.append("-1")
                break
        else:
            ans.append(f"{the_ones.pop() + 1} {the_ones.pop() + 1}")
    else:
        ans.append("-1")
print("\n".join(ans))