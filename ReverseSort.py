
for _ in range(int(input())):
    n = int(input())

    bs = input()
    sorted_bs = sorted(bs)
    def solve():
        final = []
        for i in range(n):
            if bs[i] != sorted_bs[i]:
                final.append(i+1)
        print(len(final), *final)

    if bs == "".join(sorted_bs):
        print(0)
    else:
        print(1)
        solve()