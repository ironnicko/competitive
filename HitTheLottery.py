n = int(input())
denominations = [1, 5, 10, 20, 100]
count = 0
while denominations:
    val = denominations.pop()
    if val<= n:
        count += n//val
        n%=val
print(count)