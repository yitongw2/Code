



def swap(lis,low,high):
	"swap two elements in an indexable iterable by their indices "
	temp=lis[high]
	lis[high]=lis[low]
	lis[low]=temp


def partition(lis, low, high):
	"""
	take the last item in the sequence as pivot.
	divide the sequence into 2 subsequences:
	* 1st subsequence contains items that are smaller or equal to the pivot.
	* the other subsquence contains items that are greater than the pivot.
	"""
	pivot=lis[high]
	# 2 markers: i marks the left end of the sequence and j marks the right
	# end of the sequence
	i, j=0, high-1
	while (i<=j):
		# items on the left end should be smaller than pivot
		if lis[i]>pivot:
			# find the item that is smaller or equal to pivot from
			# the right end of the sequence
			if lis[j]<=pivot:
				# swap 
				temp=lis[i]
				lis[i]=lis[j]
				lis[j]=temp
				# after swapping, move marker i one cell to the
				# right
				i+=1
			# move marker j (swapping or not)	
			j-=1
		else:
			# otherwise, move marker i one cell to the right to find
			# the item that is larger than pivot
			i+=1
	# swap the pivot back to position marked by i
	lis[high]=lis[i]
	lis[i]=pivot
	return i

def partitionK(lis,pivot):
	"""
	complicated version of partition where elements are partitioned into 3 sequences L, G and E in that particular order.
	it involves 3 different markers i, j and k. the additional marker k is used to mark the area of sequence E.
	"""
	i=0
	j=len(lis)-1
	k=len(lis)
	while (i<=j):
		# area of G and area of E is conflicted
		if j==k:
			# move marker j one cell to the left
			j=k-1
			continue
		# item of the left end is smaller than pivot
		if lis[i]<pivot:	
			# continue move the marker i to the right until a violation is found
			i+=1
			continue
		# item of the right end is greater than pivot
		if lis[j]>pivot:
			# continue move the marker j to the left until a violation is found
			j-=1
			continue
		# item of the left end equals to the pivot
		if lis[i]==pivot:
			# move marker k to the left
			k-=1
			# swap the item marked by i with the item marked by k
			swap(lis,i,k)
			continue
		if lis[j]==pivot:
			# move marker k to the left
			k-=1
			# swap the item marked by j with the item marked by k
			swap(lis,j,k)
			continue
		# violations on both end are found, swap item marked by i and item marked by j
		swap(lis,i,j)
		# move marker i to the right
		i+=1
		# move marker j to the left
		j-=1
	return (i,k)	



def isPartitioned(lis,p,i):
	"return true if an iterable is properly partitioned into less that p and greater than p"
	return all(x<p for x in lis[:i]) and all(x>=p for x in lis[i:])	



if __name__=="__main__":
	l=[3,1,4,5,3,2,33,23,3,52,53,21]
	i=partition(l, 0, len(l)-1)
	print (i)
	print (l)

