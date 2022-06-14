from collections import Counter
for _ in range(int(input())):
	n = int(input())
	q = list(map(int, input().split()))
	rem = Counter(q)
	c = set()
	ans = []
	mex = 0
	for i in range(n):
		c.add(q[i])
		while mex in c: mex += 1
		if rem[mex] == 0:
			ans.append(mex)
			c.clear()
			mex = 0
		rem[q[i]] -= 1
	print(len(ans))
	print(*ans)