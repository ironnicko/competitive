for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    res, cur = [], 0
    while nums:
        nums.sort(key=lambda i: i | cur)
        res.append(nums.pop())
        check = cur | res[-1]
        if check == cur:
            break
        cur = check
    print(*res, *nums)
