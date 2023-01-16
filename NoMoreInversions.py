"""
    Competitve Programming : Nikhil Ivannan
"""

def gcd(a, b):
    if a == 0:return b
    if b == 0: return a
    if a == b: return a
    if a > b:
        return gcd(a-b, b)

    return gcd(a, b-a)

from collections import defaultdict

n = int(input())

company = defaultdict(int)
company[1] = n
for i, x in enumerate(map(int, input().split())):
    if x != 1:
        company[x] += 1
