from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print = lambda x : stdout.write(str(x))

dp = [0 for _ in range(40002)]
dp[0] = 1
for i in range(1, 40001):
    if str(i) == str(i)[::-1]:
        for j in range(i, 40001):
            dp[j] = (dp[j]+dp[j-i])%int(1e9+7)
for _ in range(int(input())):
    print(f"{dp[int(input())]}\n")

