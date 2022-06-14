final = 0
for i in range(5):
    string = input()
    if '1' in string:
        final += abs(3 - (i+1))
        final += abs(2-string.split().index('1'))

print(final)
    
