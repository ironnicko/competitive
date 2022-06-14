from sys import stdin,stdout
input = lambda : stdin.readline().rstrip()
print =lambda x : stdout.write(str(x))

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    l = list(s)
    main_dict = {"B" : 0, "W" : 0}
    left_side = 0
    mx = 0
    for i in range(n):
        if i - left_side+1 > k:
            main_dict[s[left_side]] -= 1
            left_side+= 1
        main_dict[s[i]] += 1
        mx = max(mx, main_dict.get('B', 0))
    if mx == k: print("0\n")
    else:
        print(f"{k-mx}\n")
