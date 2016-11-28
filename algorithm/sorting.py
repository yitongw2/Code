#Comparison-based sorting
import heapq
import Code.data_structure.heap

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
	"not in-place"
	return lis


def quickSort(lis,low,high):
	if high-low<1:
		return
	else:
		pivot=lis[high]
		i=0
		j=high-1
		while (i<=j):
			if lis[i]>pivot:
				if lis[j]<=pivot:
					temp=lis[i]
					lis[i]=lis[j]
					lis[j]=temp
					i+=1	
				j-=1
			else:
				i+=1
		lis[high]=lis[i]
		lis[i]=pivot
		quickSort(lis,0,i-1)
		quickSort(lis,i,high)
			
def mergeSort(lis):  # how many recursive calls = 1+2+4+...+n
	if len(lis)<2:
		return lis   
	else:
		mid=int(len(lis)/2) 
		left=mergeSort(lis[:mid])
		right=mergeSort(lis[mid:])
		emp=[0]*(len(left)+len(right))
		#----------------merge-----------------
		i,j=0,0
		for x in range(len(emp)):   #    n 
			if j>=len(right):
				emp[x]=left[i]
				i+=1
			elif i>=len(left):
				emp[x]=right[j]
				j+=1
			elif left[i]<=right[j]:
				emp[x]=left[i]
				i+=1
			elif right[j]<left[i]:
				emp[x]=right[j]
				j+=1
			else:
				pass
		#----------------merge-----------------
		return emp

	
# integer sorting
def bucketSort(lis):
	if len(lis)<2:
		return lis
	max=lis[0]
	for x in lis:
		if x>max:
			max=x
	buck=[0]*(max+1)
	for x in lis:
		buck[x]+=1
	result=[]
	inde=0
	for x in buck:
		for y in range(x):
			result.append(inde)
		inde+=1	
	return result
		


if __name__=="__main__":
	l=[3,1,4,5,2,33,23,52,53,21]
	print (heapSort(l))
