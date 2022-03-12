no = int(input())
count =0
while no > 0:
    no -= 1
    i, j = map(int, input().split())
    count += 1 if abs(j - i) > 1 else 0
print(count)