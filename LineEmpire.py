from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print =lambda x : stdout.write(str(x)+"\n")

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    array = list(map(int, input().split()))
    sm = sum(array) 
    ans = sm * b # capturing till the last kingdom
    s = 0 # running sum counter
    for i in range(n):
        s += array[i]
        ans = min(ans, (a + b) * array[i] + (sm - s - (n-i-1) * array[i]) * b)

    print(ans)