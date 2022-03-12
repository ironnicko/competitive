for i in range(int(input())):
    n=int(input())
    numbers = [i for i in range(1, n+1)][::-1]
    for i in range(n-1, -1, -1):
        arbitrary = numbers
        arbitrary[i], arbitrary[i-1] = arbitrary[i-1], arbitrary[i]
        print(*arbitrary)