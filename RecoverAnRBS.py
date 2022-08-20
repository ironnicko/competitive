import os,sys
from re import L
from io import BytesIO,IOBase
BUFSIZ=8192
for _ in range(int(input())):
    s = input()
    n = len(s)
    open = s.count("(")
    close = s.count(")")
    open -= int(s[0] == "?")
    close -= int(s[n-1] == "?")
    buff = n - open - close
            

