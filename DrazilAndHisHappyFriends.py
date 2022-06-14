from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print =lambda x : stdout.write(str(x))

n, m = map(int,input().split())
b, *hb = [int(x) for x in input().split()]
g, *hg = [int(x) for x in input().split()]

for i in range(2*n*m):
		if (i%n) in hb and (i%m) not in hg : 
			hg.append(i%m)
		elif (i%n) not in hb and (i%m) in hg : 
			hb.append(i%n)
if len(hb) == n and len(hg) == m:
	print('Yes\n')
else:
	print('No\n')