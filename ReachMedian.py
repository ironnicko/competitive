from sys import stdin, stdout
 
 
def main():
    n, s = map(int, stdin.readline().split())
    a = [stdin.readline().split()]
    a.sort()
    operations = 0
 
    m = n // 2
 
    if a[m] < s:
        while m < len(a) and a[m] < s:
            operations += s - a[m]
            m += 1
    elif a[m] == s:
        operations = 0
    else:
        while m >= 0 and a[m] > s:
            operations += a[m] - s
            m -= 1
 
    stdout.write(str(operations) + "\n")
 
 
main()