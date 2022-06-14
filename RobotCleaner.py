for _ in range(int(input())):
    n, m, rb, cb, rd, cd = map(int, input().split())
    print(min(rd - rb if rb <= rd else 2 * n - rb - rd, cd - cb if cb <= cd else 2 * m - cb - cd))