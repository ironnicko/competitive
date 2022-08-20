# def MissingBigrams(letters=["ab", "bb", "ba", "aa", "ba"]):
#     letter = 1
#     final = letters[0]
#     ok = 1
#     while letter != len(letters):
#         if letters[letter][0] == letters[letter-1][1]:
#             final += letters[letter][1]
#         else:
#             final += letters[letter]
#             ok = 0
#         letter += 1
#     if ok: final+="a"
#     print(final)
    
# test_cases = int(input())
# while test_cases > 0:
#     test_cases -= 1
#     length = int(input())
#     letters = input().split()
#     MissingBigrams(letters)

# def SquareString(letters):
#     if len(letters)%2 == 0:
#         if letters[ :(len(letters)//2)] == letters[ (len(letters)//2)  : ]:
#             return "YES"
#         else:
#             return "NO"
#     else:
#         return "NO"

# test_cases = int(input())
# while test_cases > 0:
#     test_cases -= 1
#     letters = input()
#     print(SquareString(letters))

# import re

# def MD25(number):
#     number = list(number)
#     searchingFor = {"0" : ["5", "0"], "5" : ["7", "2"]}
#     leng = len(number)
#     count = 0
#     compare = None
#     while leng >= 0:
#         leng -= 1
#         j = leng - 1
#         if compare and j in compare:
#             return count
            
#         if number[leng] in searchingFor.keys():
#             compare = searchingFor[number[leng]]
#             if j in searchingFor[number[leng]]:
#                 return leng-j
                
#         count += 1

# testCase = int(input())
# while testCase>0:
#     testCase -= 1
#     number = input()
#     print(MD25(number))


# testCase = int(input())
# while testCase>0:
#     testCase -= 1
#     leng = int(input())
#     to_compare = {0:0, 1:0}
#     string = input()
#     if leng > 2:
#         print("NO")
#     else:
#         if leng == 2:
#             if string[0] == string[1]:
#                 print("NO")
#             else:
#                 print("YES")
#         else:
#             print("YES")

# def swap(number):
#     if number == 2:
#         print("0 1")
#         return
#     swapable = list(range(number))
#     limit = len(bin(swapable[-1])[2:])
#     set = {i: [] for i in range(1, limit+1)}
#     for number in swapable:
#         key = len(bin(number)[2:])
#         set[key].append(number)
#     result = list(set.values())
#     change = result.pop(-1)[::-1]
#     result.insert(0, change)
#     empty = []
#     [empty.extend(i) for i in result]
#     print(*empty[::-1])

# testCase = int(input())
# while testCase > 0:
#     testCase -= 1
#     swap(int(input()))

# testCase = int(input())
# while testCase > 0:
#     testCase -= 1
#     number = int(input())
#     mod = number % 7
#     lastDigit = number%10
#     if mod == 0:
#         print(number)
#         continue
    
#     if lastDigit + (7 - mod) > 9:
#         print(number - mod)
#     else:
#         print(number + (7 - mod))

# testCase = int(input())
# while testCase > 0:
#     testCase -= 1
#     number = input()
#     hashMap = {'1': 0, '0': 0}
#     for i in number:
#         hashMap[i] += 1
#     ones, zeros = hashMap["1"], hashMap["0"]
#     if ones > zeros:
#         print(zeros)
#         continue
#     elif zeros > ones:
#         print(ones)
#         continue
#     if ones == zeros:
#         print(zeros - 1)

# def KillTheMonster(hc, dc, hm, dm, k, w, a):
#     k = int(k)
#     w = int(w)
#     a = int(a)
#     original_health = int(hc)
#     original_attack = int(dc)
#     condition = ((hc + dm -1) / dm) >= ((hm + dc -1) / dc) # 44/20 >= 13/4
#     print(condition)
#     if condition:
#         return "YES"
#     else:
#         for coin in range(k+1):
#             variable = k - coin
#             hc = hc + coin * a
#             dc = dc + variable * w
#             if ((hc + dm -1) / dm) >= ((hm + dc -1) / dc):
#                 return "YES"
#             hc = original_health
#             dc = original_attack
#         else:
#             return "NO"
            
# testCase = int(input())
# while testCase>0:
#     testCase -= 1
#     character = input().split() # returning array
#     monster = input().split()
#     accessories = input().split()
#     answer = KillTheMonster(int(character[0]), int(character[1]),int( monster[0]), int(monster[1]), *accessories)
#     print(answer)

# def pleasantPairs(array: list, length: int):
#     count = 0
#     for i in range(length):
#         for j in range(i + 1, length):
#             L = i +1 + j +1
#             R = array[i] * array[j]
#             if L == R:
#                 count += 1
#             if R > 2*length : break
#     print(count)

#     # a(n-1) = (n - 1 - i) / a(i)

# testCase = int(input())
# while testCase > 0:
#     testCase -= 1
#     length = int(input())
#     elements = [int(i) for i in input().split()]
#     pleasantPairs(elements, length)

# testCase = int(input())
# while testCase>0:
#     testCase -= 1
#     money = int(input())
#     denominations = {
#         100 : 0,
#         20 : 0,
#         10 : 0,
#         5: 0,
#         1 : 0
#     }
#     copy = sorted(list(denominations.keys()))
#     ptr = -1
#     while money > 0:
#         if money >= copy[ptr]:
#             denominations[copy[ptr]] += 1
#             money -= copy[ptr]
#         else:
#             ptr -= 1
#     print(sum(denominations.values()))

# testCase = int(input())
# while testCase > 0:
#     testCase -= 1
#     length = int(input())
#     array = [int(i) for i in input().split()]
#     count = 0
#     counter = 1
#     i = len(array) - 2
#     while i >= 0:
#         if array[i] == array[-1]:
#             i -= 1
#             counter += 1
#         else:
#             i -= counter
#             count += 1
#             counter *= 2
#     print(count)

# testCase = int(input())
# while testCase>0:
#     testCase -= 1
#     length, no_of_operations =  input().split()
#     length, no_of_operations = int(length), int(no_of_operations)
#     letters =  input()

#     if letters[::-1] == letters or no_of_operations == 0:
#         print(1)
#     elif no_of_operations > 1:
#         if length%2 == 0 and letters[ : (length//2) ] == letters[ (length//2): ] :
#             print(1)
#         elif length%2 == 1 and letters[ : (length//2) ] == letters[ (length//2) + 1 : ]:
#             print(1)
#         else:
#             print(2)
#     else:
#         print(2)

# testCase = int(input())
# while testCase>0:
#     testCase -= 1
#     n, k = input().split()
#     n, k = int(n), int(k)
#     if n%2 == 1:
#         if k == 1:
#             print("YES")
#             for i in range(1, n+1):
#                 print(i)
#         else:
#             print("NO")
#     else:
#         print("YES")
#         for i in range(1, n+1):
#             sum = i
#             for j in range(1, k+1):
#                 print(sum, end=" ")
#                 sum += n

# testCase = int(input())
# X = 0
# while testCase > 0:
#     testCase -= 1
#     statement = input().strip("X").strip()
#     X = X + 1 if statement == "++" else X - 1
# print(X)

# testCase = int(input())
# while testCase > 0:
#     testCase -= 1
#     n, k = input().split()
#     n, k = int(n), int(k)
#     A = [int(i) for i in input().split()]
#     B = [int(i) for i in input().split()]
#     while n > 0:
#         n -= 1
#         if A[n] <= k:
#             k += B[n]
#             B.pop(n)
#             A.pop(n)
#             n = len(A)
#             continue
#     print(k)

# testCase = int(input())
# while testCase > 0:
#     testCase -= 1
#     l, r, k = input().split()
#     l, r, k = int(l), int(r), int(k)

#     if l == r:
#         if l > 1:
#             print("YES")
#         else:
#             print('NO')
#     else:
#         odd, even = (r - l + 1) // 2, (r - l + 1) // 2
#         if r % 2 == l % 2:
#             if r % 2 == 1:
#                 odd += 1
#             else:
#                 even += 1
#         if k >= odd:
#             print("YES")
#         else:
#             print("NO")


# def timeC(length=5, array=[1,2,3,3,4]):
#     array = sorted(array)
#     gate = True
#     variable = 0
#     result = []
#     for i in range(length):
#         if array.count(array[variable]) >= 2:
#             result.append(array.pop(variable))
#             result.append(array.pop(variable))
#             gate = False
#             break
#         variable += 1
#     if gate:
#         array.append(array.pop(1))
#         result = array
#     else:
#         copy = []
#         j = 0
#         while j < len(array):
#             if result[0] > array[j]:
#                 copy.append(array.pop(j))
#                 j -= 1
#             j += 1

#         array.extend(copy)

#         result = [result[0]] + array + [result[1]]

#     print(*result)

# testCase = int(input())
# while testCase > 0:
#     testCase -= 1
#     length = int(input())
#     array = [int(i) for i in input().split()]
#     timeC(length, array)

# testCase = int(input())
# while testCase > 0:
#     testCase -= 1
#     length = int(input())
#     array = [int(i) for i in input().split()]
#     if length == 2:
#         print(array[0], array[1], sep=" ") if array[0] < array[1] else print(array[1], array[0], sep=" ")
#         continue

#     pos, mn = -1, max(array)

#     i = 1
#     while i < length:
#         if mn > abs(array[i] - array[i - 1]):
#             pos = i
#             mn = abs(array[i] - array[i - 1])
#         i += 1
#     for i in range(pos, length):
#         print(array[i], end=" ")
#     for i in range(pos):
#         print(array[i], end=" ")

# testCase = int(input())
# while testCase > 0:
#     testCase -= 1
#     length = int(input())
#     string = input()
#     zeroes, ones = string.count("0"), string.count("1")
#     if ones>0 and zeroes==1:
#         print("BOB")
#         continue
#     if ones == length:
#         print("DRAW")
#         continue
#     if zeroes % 2 == 0 and length > 1:
#         print("BOB")
#     elif zeroes % 2 == 1 and length > 1:
#         print("ALICE")
#     elif length == 1:
#         print("BOB") if string[0] == "0" else print("ALICE")

# n, k, x = map(int, input().split())
# a = [int(i) for i in input().split()]
# a = sorted(a)

# diff = [] # make one array called difference 

# for i in range(1, n): # now we iterate through D "a" array starting from 1 through n
#     d = a[i] - a[i-1] # find D difference by subtracting second element with the first element
#     if d > x: # now append the division of difference - 1 by x [-1 is for avoiding to check for divisibility]
#         diff.append( (d-1)//x )

# diff = sorted(diff)
# n  = len(diff)

# for i in diff: # now we iterate through difference array and check if the computed result is greater than the K
#     if k >= i:
#         k -= i # we subtract the value of the element
#         n -= 1 # minus one from the size of the array to indicate that it was resolved

# print(n + 1) # finally we print the result with +1 since we start counting from the next element from the comparing element and not actually concerned about the first element

# faster fibonacci

# def fib(n=4, dic={1 : 1}):
#     if n < 2:
#         return n
#     if n in dic:
#         return dic[n]
#     dic[n] = fib(n-1, dic) + fib(n-2, dic)
#     return dic[n]
# print(fib())

# MINIMUM SUM SUBARRAY
# def mss(a):
#     mini = a[0]
#     pointer = a[0]
#     for i in range(1, len(a)):
#         num = 
#     print(mini)
# array = [20, -7, -3, 9, -4, 6, -9, 10]
# mss(array)

# def twoSum(array=[1, 5, 5, 6, 11, 3], sum=8):
#     main = set()
#     for i in array:
#         if sum-i in main:
#             print(i, sum-i)
#             break
#         else:
#             main.add(i)
# twoSum()

# n = int(input())
# a = [int(i) for i in input().split()]
# b = []
# for i in a:
#     flag = 1
#     if i == 2:
#         b.append(i)
#         continue
#     for j in range(2, i):
#         if i %j == 0:
#             flag = 0
#             break
#     if flag:
#         b.append(i)


# def canSum(i : int, memo: list):
#     s = sum(memo)
#     if not memo:
#         return False
#     elif s > i:
#         memo.remove(max(memo))
#         canSum(i, memo)
#     elif s == i:
#         return True
#     elif s < i:
#         memo.remove(min(memo))
#         canSum(i, memo)
# print(canSum(7, [5, 3, 4 , 7]))

# def non(n):
#     if n == 1:
#         return 1
#     else:
#         return n + non(n-1)
# print(non(50000))

# def recurse(day, last, dp, points):
#     if day == 0:
#         maxi = float("-inf")
#         for i in range(3):
#             if i != last:
#                 maxi = max(points[day][i], maxi)
#         return maxi
#     if dp[day][last]: return dp[day][last]
#     maxi = float("-inf")
#     for i in range(3):
#         if i != last:
#             maxi = max(points[day][i] + recurse(day-1, i, dp, points), maxi)
#     dp[day][last] = maxi
#     return dp[day][last]

# for _ in range(int(input())):
#     n = int(input())
#     points = [[int(i) for i in input().split()] for _ in range(n)]
#     dp = [[0 for __ in range(4)] for _ in range(n)]
#     print(recurse(n-1, 3, dp, points))


# from collections import OrderedDict

# class LRUCache:

# 	def __init__(self, capacity: int):
# 		self.cache = OrderedDict()
# 		self.capacity = capacity

# 	def get(self, key: int) -> int:
# 		if key not in self.cache:
# 			return -1
# 		else:
# 			self.cache.move_to_end(key)
# 			return self.cache[key]

# 	def put(self, key: int, value: int) -> None:
# 		self.cache[key] = value
# 		self.cache.move_to_end(key)
# 		if len(self.cache) > self.capacity:
# 			self.cache.popitem(last = False)


# cache = LRUCache(2)


# cache.put(1, 1)
# print(cache.cache)
# cache.put(2, 2)
# print(cache.cache)
# cache.get(1)
# print(cache.cache)
# cache.put(3, 3)
# print(cache.cache)
# cache.get(2)
# print(cache.cache)
# cache.put(4, 4)
# print(cache.cache)
# cache.get(1)
# print(cache.cache)
# cache.get(3)
# print(cache.cache)
# cache.get(4)
# print(cache.cache)


# Sieve of Eratsothenes

n = int(input())
primes = [0 for _ in range(n+1)]
for i in range(2, n+1):
    for j in range(i**2, n+1, i):
        primes[j] = 1
for i in range(n):
    if primes[i] == 0:
        print(i)