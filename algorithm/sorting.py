import heapq
import random
from partition import partition


#Comparison-based sorting

def insertionSort(lis):
	"""
	insertion sort is one type of priority-queue sort.
	Here, priority queue is implemented as a sorted array.
	Therefore, insertion takes O(n) time and removeMin() takes O(1) time.
	Imagine the priority queue starts from the left end of the array and is initially empty.
	Each time we expand the priority queue rightward, it inserts an element to the priority queue.
	"""
	for i in range(len(lis)):
		k=i
		for j in reversed(range(i)):
			if lis[j]>lis[k]:
				temp=lis[k]
				lis[k]=lis[j]
				lis[j]=temp
				k=j		

				
def selectionSort(lis):
	"""
	selection sort is still a priority queue sort.
	Here, priority queue is implemented as an unsorted array.
	Therefore, insertion takes O(1) time and removeMin() takes O(n) time.
	Imagine we separate the array into sorted area on the left end and unsorted area on the right end.
	Gradually, expand the sorted area by keep inserting the smallest element in the unsorted area to the sorted area
	and remove it from the unsorted area untill the unsorted area is empty.
	
	"""
	for x in reversed(range(len(lis))):
		ma=x
		for y in range(x):
			if lis[y]>lis[ma]:
				ma=y
		temp=lis[ma]
		lis[ma]=lis[x]
		lis[x]=temp

def heapSort(lis):
	"""
	heap sort is a type of priority queue sort where we implement priority queue as heap.
	heap is essentially a complete binary tree where the parent is smaller than any of its children.
	heapify is a fast way to construct a heap taking only O(2*n) time (bottom-up construction).
	By repeatedly poping the smallest element in the heap, we obtain a sorted array.
	"""
	heapq.heapify(lis)
	return [heapq.heappop(lis) for x in range(len(lis))]

		
def treeSort(lis):
	"""
	result=[]
	tree=AVLTree()
	for x in lis:
		tree.insert(x)
	tree.inorder_traverse(tree.root, lambda x: result.append(x))	
	return result
	"""
	pass


	
def quickSort(lis, low, high):
	"""
	(non randomized) quick sort.
	if low>high, nothing left to sort.
	else, choose the pivot at the end of sequence and partition it into
	2 subsequences. Then, recurse on both of the subsequences.  
	"""
	if high-low<1:
		return
	else:
		i=partition(lis, low, high)
		quickSort(lis, low, i-1)
		quickSort(lis, i, high)

def randomQuickSort(lis, low, high):
	"""
	variation of quick sort.
	difference: choose pivot randomly.
	better avg performance since more likely to partition the sequence
	into 2 equal-sized subsequences.
	"""
	if high-low<1:
		return
	else:
		pivot_index=random.randint(low, high)
		temp=lis[pivot_index]
		lis[pivot_index]=lis[high]
		lis[high]=temp
		i=partition(lis, low, high)
		randomQuickSort(lis, low, i-1)
		randomQuickSort(lis, i, high)
	
def merge(left, right):
	"""
	merge 2 sequences left and right into 1 sorted sequence.
	"""
	result=[0]*(len(left)+len(right))
	# marker i for left, marker j for right
	i,j=0,0
	for x in range(len(result)):  
		# all items of right sequence have been pushed into result, 
		# then push all items of left sequence into result.
		if j>=len(right):
			result[x]=left[i]
			i+=1
                # all items of left sequence have been pushed into result, 
                # then push all items of right sequence into result.
		elif i>=len(left):
			result[x]=right[j]
			j+=1
		elif left[i]<=right[j]:
			result[x]=left[i]
			i+=1
		elif right[j]<left[i]:
			result[x]=right[j]
			j+=1
	return result
	
		
def mergeSort(lis):  
	# how many recursive calls = 1+2+4+...+n
	if len(lis)<2:
		return lis   
	else:
		mid=int(len(lis)/2)
		left=mergeSort(lis[:mid])
		right=mergeSort(lis[mid:])
		return merge(left, right)

	


# Integer sorting

def bucketSort(lis, size, hash=lambda x: int(x)):
	# if there are less then 2 elements in the collection, 
	# 	sequence of 1 element is already sorted
	if len(lis)<2:
		return lis
	
	# create a list of buckets
	buckets=[[] for x in range(size)]
	
	for item in lis:
		# obtain index by hash function
		# locate the correct bucket and append the item to the bucket
		buckets[hash(item)].append(item)
	
	result=[]
	# loop through buckets in the order of the index
	for bucket in buckets:
		for item in bucket:
			# push items in the bucket to the result
			result.append(item)
	return result	


def baseB(x, b=2, fd=0):
	"""
	represents a number x in base b (by default base is 2).
	if number x is not within the range that the base can be directly 
	represented (without carry), divide the number x by base b and recurse
	on the result of the ceilling of x/b first.
	finally, represents the least significant digit by taking the modulo
	of b.
	if specified, the representation can be maintained to have a fixed 
	digit (by default, fd is 0). 
	"""
	repr=""
	if x>=b:
		# speed-up trick: bitwise operator since it is faster than 
		# normal opertor. 
		# here, could use x<<b. 
		repr+=baseB(x//b, b)
	# modulo can also be replaced by 
	repr+=str(x%b)
	if len(repr)<fd:
		repr="0"*(fd-len(repr))+repr
	return repr


def radixSort(lis):
	# choose base to be n (or near 2 to the number of items to be sorted
	base=len(lis)
	# find the range of items in the sequence by finding the max item
	maxKey=max(lis)
	# calculates how many digits are required to represent the max item
	digits=len(baseB(maxKey, base))

	# loop through the digits starting from the least significant digit
	for digit in reversed(range(digits)):
		# perform a bucket sort on the sequence based on the current
		# digit 
		lis=bucketSort(lis, maxKey, lambda x: \
			int(baseB(x, base, digits)[digit]))
	return lis
	

if __name__=="__main__":
	#l=[3,1,4,5,2,33,23,52,53,21]
	l=[random.randint(0,1000) for x in range(10)]
	print (radixSort(l))
