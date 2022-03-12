testCase = int(input())
X = 0
while testCase > 0:
    testCase -= 1
    statement = input().strip("X")
    X = X + 1 if statement == "++" else X - 1
print(X)