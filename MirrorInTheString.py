for _ in range(int(input())):
    n=int(input())
    s=(input().strip())
    k=1 
    while (k < n and (s[k] < s[k - 1] or (k > 1 and s[k] == s[k - 1]))):
        k+=1 
    ans = s[ : k]
    print( ans+ans[::-1] )