a = input()
b = input()
n = len(a)
m = len(b)

count = [0]
for i in a:
    count.append(count[-1] + int(i == '1'))

ans = 0
for i in range(m, n):
    sub = count[i ] - count[i-m]
    ans += (b.count('1') & 1 == sub & 1)

print(ans)
