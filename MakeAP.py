t = int(input())
for i in range(t):
	nums = input().split()
	nums = list(map(int,nums))
	if (nums[0]+nums[2]) % 2*nums[1] == 0:
		print('YES')
	elif (2 * nums[1] - nums[0]) % nums[2] == 0 and 2 * nums[1] - nums[0] > 0:
		print('YES')
	elif (2*nums[1]-nums[2]) % nums[0] == 0 and 2 * nums[1] - nums[2] > 0:
		print('YES')
	else:
		print('NO')