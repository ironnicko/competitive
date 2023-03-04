class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & (-i)

    def get(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s

for _ in range(int(input())):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    bit = BIT(n)
    for __ in range(q):
        t, *res = map(int, input().split())
        if t == 1:
            l, r = res
            bit.update(l, 1)
            bit.update(r+1, -1)
        else:
            res = int(res[0])
            times = bit.get(res)
            item = arr[res - 1]
            for i in range(times):
                if item < 10:
                    break
                item = sum(map(int, list(str(item))))
            print(item)
