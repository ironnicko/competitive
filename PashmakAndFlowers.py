input()
l = sorted(map(int, input().split()))
a = l[0]
b = l[-1]
c = len(l)
print(b-a, a != b and l.count(a) * l.count(b) or c*(c-1)//2)