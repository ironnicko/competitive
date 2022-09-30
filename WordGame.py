n = int(input())
for _ in range(n):
  one1=input().split()
  one2=input().split()


  one3=input().split()

  ONE1 = set(one1)
  s2 = set(one2)


  s3 = set(one3)
  MOD = 1000000 + 7
  SETfirst= ONE1.intersection(s2) 



  SETSecind=ONE1.intersection(s3)
  SET=s2.intersection(s3)

  X1=len(SETfirst)
  Z1=len(SET)
  y=len(SETSecind)

  RS = SETfirst.intersection(s3)
  FL = list(RS)
  nextSET=len(RS)

  a=3*(len(one1)-X1-y+nextSET) + X1+y-nextSET-nextSET


  b=3*(len(one2)-X1-Z1+nextSET)+X1+Z1-nextSET-nextSET
  c=3*(len(one3)-y-Z1+nextSET)+Z1+y-nextSET-nextSET
  
  print(a%MOD, b%MOD, c%MOD)