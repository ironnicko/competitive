
for _ in range(int(input())):
    input()
    Xa,Ya = map(int,input().split())
    Xb,Yb = map(int,input().split())
    Xf,Yf = map(int,input().split())
    cond = int(((Xa==Xb==Xf) and (Ya<Yf<Yb or Ya>Yf>Yb))or ((Ya==Yf==Yb) and (Xa<Xf<Xb or Xa>Xf>Xb)))
    score = abs(Xa-Xb)+abs(Ya-Yb) + 2 * int(cond)
    print(score)
    