n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

pref = [0]

for i in range(n):
    pref.append(pref[-1] + (A[i] * B[i]))
ans = pref[-1]

for i in range(n):
    # ODD
    state = A[i] * B[i]
    l = i - 1
    r = i + 1
    while l > -1 and r < n:
        state += (A[l] * B[r])
        state += (A[r] * B[l])
        ans = max(ans, state + pref[l] + (pref[n] - pref[r + 1]))
        l -= 1
        r += 1

    # EVEN
    state = 0
    l = i
    r = i + 1
    while l > -1 and r < n:
        state += (A[l] * B[r])
        state += (A[r] * B[l])
        ans = max(ans, state + pref[l] + (pref[n] - pref[r + 1]))
        l -= 1
        r += 1

print(ans)
