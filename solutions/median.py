
def findMedian(lis):
	"""
	find the median of a sequence by simply sorting them and obtain the item 
	in the cell with index at the middle.
	"""
	m=len(lis)//2
	l=sorted(lis)
	return l[m] if len(l)%2!=0 else (l[m-1]+l[m])/2
