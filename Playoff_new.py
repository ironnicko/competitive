n = int(input())

s = input()

final = (1 << n) - (1 << (n - s.count('1')))
initial = 1 << s.count('1')

print(*range(initial, final + 2))
