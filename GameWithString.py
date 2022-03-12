s = input()
stack = []
count = 0
for i in range(len(s)):
	if len(stack) == 0:
		stack.append(s[i])
	
	else:
		if s[i] == stack[len(stack) - 1]:
			stack.pop()
			count += 1
		else:
			stack.append(s[i])

if count & 1 :
	print('Yes')
else:
	print('No')