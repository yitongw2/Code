

def power_mod(x, y, z):
	"""
	x^y mod z
	short cut: x^y ==> (x^(y/2))^2
	"""
	if y==0:
<<<<<<< HEAD
		return 1%z
=======
		return 1
>>>>>>> 400dbcbe327c270e11e8aa5293daa5a90f95ef8a
	if y==1:
		return x%z
	a=power_mod(x, y//2, z)
	if y%2==0:
		return (a*a)%z
	else:
		return (x*a*a)%z

			


if __name__=="__main__":
	print (power_mod(2, 4, 5))
		

