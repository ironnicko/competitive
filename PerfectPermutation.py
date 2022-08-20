from math import gcd
def leftRotate(arr, d, n):
    for i in range(gcd(d,n)):
         

        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
 
for _ in range(int(input())):
    n = int(input())
    print(n, end=" ")
    for i in range(1, n):
        print(i, end=" ")
    print()