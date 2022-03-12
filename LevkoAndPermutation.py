from operator import truediv


n, k = map(int, input().split())
gate = True
if k > n-1:
    gate = False

operations = n - k -1
current, last = 0, n-1
numbers = list(range(1, n+1))

while operations > 0 and k < n-1 and gate:
    operations -= 1
    numbers[current], numbers[last] = numbers[last], numbers[current]
    last -= 1

print(*numbers) if gate else print(-1)
