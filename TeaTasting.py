from heapq import heappush, heappop

# class BIT:
#     def __init__(self, n=0, arr=[]):
#         if arr:
#             n = len(arr)
#         self.n = n
#         self.bit = [0] * (n + 2)
#         if arr:
#             self.const(arr)

#     def update(self, i, x):
#         while i <= self.n:
#             self.bit[i] += x
#             i += i & (-i)

#     def get(self, i, cons=None):
#         s = 0
#         while i > 0:
#             if cons:
#                 safe = min(self.bit[i], cons)
#                 s += safe
#                 self.update(i, -safe)
#             else:
#                 s += self.bit[i]
#             i -= i & (-i)
#         return s

#     def const(self, arr):
#         for i, x in enumerate(arr, start=1):
#             self.update(i, x)


# def solve():
#     n = int(input())
#     tea = list(map(int, input().split()))
#     tas = list(map(int, input().split()))

#     bp_tea = BIT(n)

#     for i in range(1, n+1):
#         bp_tea.update(i, tea[i-1])
#         g_tea = bp_tea.get(i, tas[i-1]) + bp_tea.get(i-1, tas[i-1])
#         print(g_tea, end=" ")

#     print()


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    psum = [0] * (n+1)
    for i in range(n):
        psum[i] = psum[i-1] + b[i]

    ans = [0] * n
    h = []
    for i in range(n):
        suff = psum[-1] - psum[i]
        heappush(h, (a[i]-suff, i))

        while h:
            val, ci = h[0]
            suff = psum[-1] - psum[ci]
            val += suff

            if val <= psum[i]-psum[ci-1]:
                ans[i] += val - (psum[i-1]-psum[ci-1])
                heappop(h)
            else:
                break

        ans[i] += b[i]*len(h)

    print(*ans)


for _ in range(int(input())):
    solve()
