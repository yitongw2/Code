def findMaxSubArray(l):
	"""
	find the maximum subarray in an findMaxSubArray
	time complexity: O(n)
	memory space: O(n)
	"""
	
	r=0
	s=[]
	for x in range(len(l)):
		r+=l[x]
		s.append(r)
	print (s)
	i,j=0,len(l)-1
	for x in range(len(l)):
		if l[x]>l[j]:
			j=x
	for x in range(j):
		if l[x]<l[i]:
			i=x 
	if i==0:
		return (i,j)
	return (i+1,j)



if __name__=="__main__":
	l=[-2,-4,3,-1,5,6,-7,-2,4,-3,2]
	l1=[1,2,3,4,5,6,7]
	l2=[-2,-4,3,-1,5,6,-7,-2,4,-3,2]
	print (findMaxSubArray(l))
	print (findMaxSubArray(l1))
	print (findMaxSubArray(l2))
