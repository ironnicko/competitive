for t in range(int(input())):
  k,x=map(int,input().split())
  l=0
  r=2*k-1
  if x<k*k:
    while r-l>1:
      m=(l+r)//2
      if m<=k:
          s=m*(m+1)//2
      else:
          s=k*k-(2*k-1-m)*(2*k-m)//2
      if s<x:
          l=m
      else:
          r=m
  print(r)