
n = int(input())

players = list(zip(list(map(int, input().split())),
               list(map(int, input().split()))))

a, b = 0, 0
def recurr(i, total, pick=-1):
    if i < 0:
        return total
    if pick != -1:
        take = recurr(i-1, total+players[i][1-pick], 1-pick)
        notTake = recurr(i-1, total)
        return max(take, notTake)
    else:
        take = max(recurr(i-1, total+players[i][0], 0), recurr(i-1, total+players[i][1], 1))
        notTake = recurr(i-1, total)
        return max(notTake, take)

# print(recurr(len(players) - 1, 0))
for i in range(n):
    a,b = max(a, b + players[i][1]), max(b, a + players[i][0])
print(max(a,b))