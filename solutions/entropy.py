import math

def entropy(p,n):
	s=(float)(n+p)
	pp=p/s
	np=n/s
	fir=pp*math.log(1/pp,2) if pp!=0 else 0
	sec=np*math.log(1/np,2) if np!=0 else 0 
	return fir+sec

def ig(p1,pp1,p2,pp2,e):
	return e-(p1*pp1+p2*pp2)

root=entropy(4,6)
left=entropy(3,4)
right=entropy(1,2)
lp=7/10
rp=3/10
print (root)
print (left)
print (right)
print (lp)
print (rp)
print (ig(lp,left,rp,right,root))
