def get2Count(k):
	cnt = 0
	while k % 2 == 0:
		k = k // 2
		cnt += 1
	return cnt
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    op = []
    for i in range(n):
        count += get2Count(arr[i])
        op.append(get2Count(i+1))
    
    if count + sum(op) < n:
        print("-1")
    else:
        op.sort(reverse=1)
        ans = 0
        for i in op:
            if count >= n:
                break
            count += i
            ans += 1
        print(ans)