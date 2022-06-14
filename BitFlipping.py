T = int(input())
for _ in range(T):
  n, k = map(int, input().split())
  kc = k
  s = input()
  ans = list(s)
  flip = [0]*n
  if k%2:
    for i in range(n):
      if k == 0:
        break
      if s[i] == '1':
        flip[i] = 1
        k -= 1
    if k > 0:
      flip[-1] += k
  else:
    for i in range(n):
      if k == 0:
        break
      if s[i] == '0':
        flip[i] = 1
        k -= 1
    if k > 0:
      flip[-1] += k
  mapp = {'1':'0', '0':'1'}
  for i in range(n):
    if (kc-flip[i])%2:
      ans[i] = mapp[ans[i]]
  print(''.join(ans))
  print(' '.join([str(f) for f in flip]))
  # print(flip)