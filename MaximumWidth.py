n,m = map(int, input().split())
s = input()
t = input()
left = [0] * m
right = [0] * m
i  = 0
j = 0
while i < n and j < m:
    if s[i] == t[j]:
        left[j] = i
        j += 1
    i+=1
i = n - 1
j = m -1
while i > -1 and j > -1:
    if s[i] == t[j]:
        right[j] = i
        j -= 1
    i-=1
res= 0
for i in range(1, m):
    res = max(right[i] -  left[i-1], res)
print(res)