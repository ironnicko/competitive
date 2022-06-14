# since any number can be made with the combination (A * 11 + B * 111)
for _ in range(int(input())):
    n = int(input())
    if n >= 111 * (n%11):
        print("YES")
    else:
        print("NO")