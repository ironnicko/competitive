from sys import stdin,stdout
from collections import deque
input = stdin.readline
print = stdout.write

for _ in range(int(input())):
    na = int(input())
    alice = [int(i) for i in input().rstrip().split()]
    nb = int(input())
    bob = [int(i) for i in input().rstrip().split()]
    if max(bob) > max(alice):
        print("Bob\nBob\n")
    elif max(alice) > max(bob):
        print("Alice\nAlice\n")
    else:
        print("Alice\nBob\n")
