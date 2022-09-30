 
for _ in range(int(input())):

	s = input()
	n = len(s)
	arr = [(ord(s[i]), i + 1)  for i in range(1, n - 1)]

	first = ord(s[0])
	last = ord(s[-1])
	mn = abs(first - last)
	if first <= last:
		arr.sort()
	else:
		arr.sort(reverse=True)

	ans = [1]

	for i, j in arr:

		if i >= first and i <= last:
			ans.append(j)
		elif i <= first and i >= last:
			ans.append(j)
	ans.append(n)
	print(mn, len(ans))
	for i in ans:
		print(i, end=' ')


	print()



