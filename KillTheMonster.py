from math import ceil

t=int(input())
for _ in range(t):
	hc,dc=map(int, input().split())
	hm,dm=map(int, input().split())
	k,w,a=map(int, input().split())
	out='NO'

	for i in range(k+1):
		hcc=hc+i*a
		dcc=dc+(k-i)*w

		if ceil(hm/dcc)<=ceil(hcc/dm):
			out='YES'
			break
	
	print(out)