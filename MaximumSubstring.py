import os
import sys
def input(): return sys.stdin.readline().rstrip("\r\n")
def print(x): return sys.stdout.write(str)


MOD = int(2e5 + 1)
for _ in range(int(input())):
    binary_size = int(input()) % MOD
    binary_string = input()

    o1 = binary_string.count("1") % MOD
    z0 = binary_string.count("0") % MOD

    final = o1 * z0

    soFar = [
        min(0+1, z0),
        min(1+0, o1)
    ]
    another = [0, 0]
    for i in range(1, binary_size):
        if binary_string[i-1] == binary_string[i]:
            soFar[int(binary_string[i])] += 1
        else:
            another[0] = max(another[0], soFar[0])
            another[1] = max(another[1], soFar[1])
            soFar = [min(1, z0), min(1, o1)]
    final = max(final, pow(max(soFar[1], another[1]), 2), pow(
        max(soFar[0], another[0]), 2))
    print(final)
    print("\n")
