for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    if nums[0]:
        ans = [n+1]+list(range(1, n+1))
    elif not nums[-1]:
        ans = list(range(1, n+2))
    else:
        ans = []
        for i in range(n):
            ans.append(i+1)
            if nums[i+1] and not nums[i]:
                ans.append(n+1)
                ans.extend(list(range(i+2, n+1)))
                break
    print(' '.join(map(str, ans)))
