
def ksb_multi(I, J):
	# determines how many digits are there 
	# bin(I) converts an integer into a binary string '0bxx' with prefix 0b
	digits=max(len(bin(I)),len(bin(J)))-2
	# base case (could vary depending on needs)
	if digits==1:
		return I*J
	# calculate the number of positions needed to shift rightward in order 
	# to obtain high order bits 
	high_order=digits//2
	# shift bits of I and J rightward by the number of positions specified 
	# by high_order 
	Ih=I>>high_order
	Jh=J>>high_order
	# (1<<high_order)-1 creates a mask similar to 00001111 where low-order
	# bits are all 1 and high-order bits are all 0.
	# when performing a bitwise and operation with I, it masks off the low
	# -order part and keeps the high-order part
	Il=I&((1<<high_order)-1)
	Jl=J&((1<<high_order)-1)
	# recursively compute Ih*Jh, Il*Jl and (Ih+Jh)*(Il+Jl)
	p=ksb_multi(Ih, Jh)
	q=ksb_multi(Il, Jl)
	r=ksb_multi(Ih+Il, Jh+Jl)-p-q
	# shifting the positions back
	return (p<<(high_order*2))+q+(r<<high_order)

if __name__=="__main__":
	print (ksb_multi(23,54))
	print (23*54)

