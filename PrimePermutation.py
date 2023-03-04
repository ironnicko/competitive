from collections import Counter
import os
import sys
from io import BytesIO, IOBase
BUFSIZ = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "n" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZ))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZ))
            self.newlines = b.count(b"\n")+(not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)


def input(): return sys.stdin.readline().rstrip("\r\n")


def solve():
    s = input()
    n = len(s)
    if n < 4:
        print("YES")
        print(s)
        return

    # Getting the primes till N

    ps = [_ & 1 if _ != 1 else 0 for _ in range(n+1)]
    primes = [2]
    for i in range(2, n+1):
        if i == 1:
            continue
        cnt = i
        
        while i * cnt < n:
            ps[i * cnt] = 0
            cnt += 2
        if ps[i]:
            primes.append(i)

    count = Counter(s)
    com = count.most_common()[0][0]

    # every symbol except first until n // 2 should have to be the same.
    # imagine we have prime P, then next prime for that number will be 2 * P.
    # if 2 * P <= N, then this should be the same number as 2

    ans = ["" for _ in range(n)]
    for prime in primes:
        if prime > n:
            break
        if prime <= n >> 1:
            for i in range(prime - 1, n, prime):
                if not ans[i]:
                    ans[i] = com
                    count[com] -= 1
                    if count[com] < 0:
                        print("NO")
                        return

    # Deal with leftovers

    for i in range(n):
        if not ans[i]:
            while not count[next(iter(count))[0]]:
                del count[next(iter(count))[0]]
            k = next(iter(count))[0]
            ans[i] = k
            count[k] -= 1

    print("YES", "".join(ans), sep="\n")


solve()
